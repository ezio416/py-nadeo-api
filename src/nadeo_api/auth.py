'''
- Functions for interacting with authentication tokens to use with the API
- Also contains variables and functions intended for internal use
'''

from base64 import b64encode, urlsafe_b64decode
from dataclasses import dataclass
from datetime import datetime as dt
import json
import time

import requests

from . import config
from . import util


AUDIENCE_CORE:  str = 'NadeoServices'
AUDIENCE_LIVE:  str = 'NadeoLiveServices'  # also used for Meet endpoints (formerly known as Club)
AUDIENCE_OAUTH: str = 'OAuth2'
URL_CORE:       str = 'https://prod.trackmania.core.nadeo.online'
URL_LIVE:       str = 'https://live-services.trackmania.nadeo.live'
URL_MEET:       str = 'https://meet.trackmania.nadeo.club'
URL_OAUTH:      str = 'https://api.trackmania.com'


@dataclass
class JSONWebToken:
    '''
    - a JSON web token in a base64-encoded string
    '''

    decoded: dict
    token:   str

    def __init__(self, token: str):
        self.token = token

        try:
            self.decoded = self.decode(token)
        except IndexError, UnicodeDecodeError:
            util._log(f'failed to decode token: {self.token}')

    def __repr__(self) -> str:
        return f"nadeo_api.auth.JSONWebToken('{self.token}')"

    def __str__(self) -> str:
        return self.token

    @staticmethod
    def decode(token: str) -> dict:
        '''
        - decodes a JSON web token into a dictionary using its payload section
        - will fail if passed an invalid token
        '''

        payload:       str = token.split('.')[1]
        decoded_bytes: bytes = urlsafe_b64decode(f'{payload}==')
        decoded_str:   str = decoded_bytes.decode('utf-8')
        result:        dict = json.loads(decoded_str)

        return result


@dataclass
class Token:
    '''
    - a general authentication token
    - does not contain a base URL as a token could be used for multiple

    Parameters
    ----------
    audience: str
        - audience for which token is valid

    access_token: str
        - main token used for authorization

    refresh_token: str
        - token used to refresh access token (if applicable)
        - default: `''` (empty)

    expiration: int
        - time at which access token will expire
        - if not given, will be decoded from the token's payload
        - default: `0`
    '''

    access_token:   JSONWebToken
    audience:       str
    expiration:     int
    refresh_token:  JSONWebToken

    def __init__(self, audience: str, access_token: str, refresh_token: str = '', expiration: int = 0):
        self.audience = self.verify_audience(audience)
        self.access_token = JSONWebToken(access_token)
        self.refresh_token = JSONWebToken(refresh_token)

        if expiration:
            self.expiration = expiration
        else:
            try:
                self.expiration = self.access_token.decoded['exp']
            except KeyError:
                util._log("decoded token missing key 'exp'")
                self.expiration = int(time.time()) + 3600

    def __repr__(self) -> str:
        return f"nadeo_api.auth.Token('{self.audience}', '{self.access_token}', '{self.refresh_token}', {self.expiration})"

    def __str__(self) -> str:
        return self.access_token.token

    @property
    def expired(self) -> bool:
        return int(time.time()) >= self.expiration

    @staticmethod
    def verify_audience(audience: str) -> str:
        lower: str = audience.lower()

        if lower in ('nadeoservices', 'core', 'prod'):
            return AUDIENCE_CORE

        if lower in ('nadeoliveservices', 'live', 'meet', 'club'):
            return AUDIENCE_LIVE

        if lower in ('oauth', 'oauth2'):
            return AUDIENCE_OAUTH

        raise ValueError(f'invalid audience: {audience}')


class OAuthToken(Token):
    '''
    - a token for the public Trackmania API
    - learn more about the API here: https://webservices.openplanet.dev/oauth/auth

    Parameters
    ----------
    access_token: str
        - main token used for authorization

    expiration: int
        - time at which access token will expire
        - if not given, will be decoded from the token's payload
        - default: `0`
    '''

    def __init__(self, access_token: str, expiration: int = 0):
        super().__init__(AUDIENCE_OAUTH, access_token, '', expiration)

    def __repr__(self) -> str:
        return f"nadeo_api.auth.OAuthToken('{self.access_token}', {self.expiration})"

    @staticmethod
    def get(identifier: str, secret: str) -> OAuthToken:
        '''
        - requests an authentication token

        Parameters
        ----------
        identifier: str
            - username

        secret: str
            - password
        '''

        req: requests.Response = requests.post(
            f'{URL_OAUTH}/api/access_token',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data={
                'grant_type':    'client_credentials',
                'client_id':     identifier,
                'client_secret': secret
            }
        )

        if req.status_code >= 400:
            raise ConnectionError(f'failed to get token: code {req.status_code}, response {req.text}')

        json: dict = req.json()
        util._log('got OAuth2 token')
        return OAuthToken(json['access_token'], int(time.time()) + json['expires_in'])


class WebServicesToken(Token):
    '''
    - a token for the private web services API

    Parameters
    ----------
    audience: str
        - audience for which token is valid

    access_token: str
        - main token used for authorization

    refresh_token: str
        - token used to refresh access token

    expiration: int
        - time at which access token will expire
        - if not given, will be decoded from the token's payload
        - default: `0`
    '''

    def __init__(self, audience: str, access_token: str, refresh_token: str, expiration: int = 0):
        super().__init__(audience, access_token, refresh_token, expiration)

    def __repr__(self) -> str:
        return f"nadeo_api.auth.WebServicesToken('{self.audience}', '{self.access_token}', '{self.refresh_token}', {self.expiration})"

    def refresh(self) -> None:
        '''
        - refreshes access and refresh tokens
        '''

        req: requests.Response = requests.post(
            f'{URL_CORE}/v2/authentication/token/refresh',
            headers={'Authorization': self.refresh_token},
            # json={'audience': self.audience}  # seems to not actually be required
        )

        if req.status_code >= 400:
            raise ConnectionError(f'failed to refresh token: code {req.status_code}, response {req.text}')

        json: dict = req.json()
        self.access_token = JSONWebToken(f'nadeo_v1 t={json['accessToken']}')
        self.refresh_token = JSONWebToken(f'nadeo_v1 t={json['refreshToken']}')
        util._log('refreshed token')

        try:
            self.expiration = self.access_token.decoded['exp']
        except KeyError:
            util._log("decoded token missing key 'exp'")
            self.expiration = 0

    @staticmethod
    def get(audience: str, login: str, password: str, agent: str) -> WebServicesToken:
        '''
        - requests a web services token for a given audience
        - this token is not useful on its own, instead use a token for a specific account type

        Parameters
        ----------
        audience: str
            - desired audience for token use
            - capitalization is ignored
            - valid: `'NadeoServices'`/`'core'`/`'prod'`, `'NadeoLiveServices'`/`'live'`/`'meet'`/`'club'`

        login: str
            - account username

        password: str
            - account password

        agent: str
            - user agent, ideally with your program's name and a way to contact you
            - Nadeo can block your request without this being properly set
        '''

        Token.verify_audience(audience)

        if not agent:
            raise ValueError('user agent is required')

        req: requests.Response = requests.post(
            f'{URL_CORE}/v2/authentication/token/basic',
            headers={
                'Authorization': f'Basic {b64encode(f'{login}:{password}'.encode('utf-8')).decode('ascii')}',
                'Content-Type':  'application/json',
                'User-Agent':    agent,
            },
            json={'audience': audience}
        )

        if req.status_code >= 400:
            raise ConnectionError(f'failed getting token: code {req.status_code}, response {req.text}')

        json: dict = req.json()
        util._log('got web services token')
        return WebServicesToken(audience, f'nadeo_v1 t={json['accessToken']}', f'nadeo_v1 t={json['refreshToken']}')


class DedicatedServerToken(WebServicesToken):
    '''
    - a token for the private web services API
    - learn more about a dedicated server account here: https://webservices.openplanet.dev/auth/dedi

    Parameters
    ----------
    audience: str
        - audience for which token is valid

    access_token: str
        - main token used for authorization

    refresh_token: str
        - token used to refresh access token

    expiration: int
        - time at which access token will expire
        - if not given, will be decoded from the token's payload
        - default: `0`
    '''

    def __init__(self, audience: str, access_token: str, refresh_token: str, expiration: int = 0):
        super().__init__(audience, access_token, refresh_token, expiration)

    def __repr__(self) -> str:
        return f"nadeo_api.auth.DedicatedServerToken('{self.audience}', '{self.access_token}', '{self.refresh_token}', {self.expiration})"

    @staticmethod
    def get(audience: str, login: str, password: str, agent: str) -> DedicatedServerToken:
        '''
        - requests a dedicated server account token for a given audience

        Parameters
        ----------
        audience: str
            - desired audience for token use
            - capitalization is ignored
            - valid: `'NadeoServices'`/`'core'`/`'prod'`, `'NadeoLiveServices'`/`'live'`/`'meet'`/`'club'`

        login: str
            - dedicated server account username

        password: str
            - dedicated server account password

        agent: str
            - user agent, ideally with your program's name and a way to contact you
            - Nadeo can block your request without this being properly set
        '''

        token: WebServicesToken = WebServicesToken.get(audience, login, password, agent)
        util._log('got dedicated server token')
        return DedicatedServerToken(token.audience, token.access_token.token, token.refresh_token.token, token.expiration)


class ServiceToken(WebServicesToken):
    '''
    - a token for the private web services API
    - learn more about a service account here: https://webservices.openplanet.dev/auth/service

    Parameters
    ----------
    audience: str
        - audience for which token is valid

    access_token: str
        - main token used for authorization

    refresh_token: str
        - token used to refresh access token

    expiration: int
        - time at which access token will expire
        - if not given, will be decoded from the token's payload
        - default: `0`
    '''

    def __init__(self, audience: str, access_token: str, refresh_token: str, expiration: int = 0):
        super().__init__(audience, access_token, refresh_token, expiration)

    def __repr__(self) -> str:
        return f"nadeo_api.auth.ServiceToken('{self.audience}', '{self.access_token}', '{self.refresh_token}', {self.expiration})"

    @staticmethod
    def get(audience: str, login: str, password: str, agent: str) -> ServiceToken:
        '''
        - requests a service account token for a given audience

        Parameters
        ----------
        audience: str
            - desired audience for token use
            - capitalization is ignored
            - valid: `'NadeoServices'`/`'core'`/`'prod'`, `'NadeoLiveServices'`/`'live'`/`'meet'`/`'club'`

        login: str
            - service account username

        password: str
            - service account password

        agent: str
            - user agent, ideally with your program's name and a way to contact you
            - Nadeo can block your request without this being properly set
        '''

        token: WebServicesToken = WebServicesToken.get(audience, login, password, agent)
        util._log('got service token')
        return ServiceToken(token.audience, token.access_token.token, token.refresh_token.token, token.expiration)


def _delete(token: Token, base_url: str, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a DELETE request to a specified API
    - this is for internal use - you should use an API-specific `delete` function instead

    Parameters
    ----------
    token: Token
        - authentication token

    base_url: str
        - base URL of desired API
        - must match your token's audience
        - valid: `URL_CORE`, `URL_LIVE`, `URL_MEET`, `URL_OAUTH`

    endpoint: str
        - desired endpoint or full URL
        - base URL and leading slash (`'https://.../'`) optional

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated
        - default: `{}` (empty)

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return _request(token, base_url, endpoint, params, 'delete', body)


def _get(token: Token, base_url: str, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a GET request to a specified API
    - this is for internal use - you should use an API-specific `get` function instead

    Parameters
    ----------
    token: Token
        - authentication token

    base_url: str
        - base URL of desired API
        - must match your token's audience
        - valid: `URL_CORE`, `URL_LIVE`, `URL_MEET`, `URL_OAUTH`

    endpoint: str
        - desired endpoint or full URL
        - base URL and leading slash (`'https://.../'`) optional

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return _request(token, base_url, endpoint, params)


def _head(token: Token, base_url: str, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a HEAD request to a specified API
    - this is for internal use - you should use an API-specific `head` function instead

    Parameters
    ----------
    token: Token
        - authentication token

    base_url: str
        - base URL of desired API
        - must match your token's audience
        - valid: `URL_CORE`, `URL_LIVE`, `URL_MEET`, `URL_OAUTH`

    endpoint: str
        - desired endpoint or full URL
        - base URL and leading slash (`'https://.../'`) optional

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return _request(token, base_url, endpoint, params, 'head')


def _options(token: Token, base_url: str, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends an OPTIONS request to a specified API
    - this is for internal use - you should use an API-specific `options` function instead

    Parameters
    ----------
    token: Token
        - authentication token

    base_url: str
        - base URL of desired API
        - must match your token's audience
        - valid: `URL_CORE`, `URL_LIVE`, `URL_MEET`, `URL_OAUTH`

    endpoint: str
        - desired endpoint or full URL
        - base URL and leading slash (`'https://.../'`) optional

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated
        - default: `{}` (empty)

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return _request(token, base_url, endpoint, params, 'options', body)


def _patch(token: Token, base_url: str, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PATCH request to a specified API
    - this is for internal use - you should use an API-specific `patch` function instead

    Parameters
    ----------
    token: Token
        - authentication token

    base_url: str
        - base URL of desired API
        - must match your token's audience
        - valid: `URL_CORE`, `URL_LIVE`, `URL_MEET`, `URL_OAUTH`

    endpoint: str
        - desired endpoint or full URL
        - base URL and leading slash (`'https://.../'`) optional

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated
        - default: `{}` (empty)

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return _request(token, base_url, endpoint, params, 'patch', body)


def _post(token: Token, base_url: str, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a POST request to a specified API
    - this is for internal use - you should use an API-specific `post` function instead

    Parameters
    ----------
    token: Token
        - authentication token

    base_url: str
        - base URL of desired API
        - must match your token's audience
        - valid: `URL_CORE`, `URL_LIVE`, `URL_MEET`, `URL_OAUTH`

    endpoint: str
        - desired endpoint or full URL
        - base URL and leading slash (`'https://.../'`) optional

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated
        - default: `{}` (empty)

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return _request(token, base_url, endpoint, params, 'post', body)


def _put(token: Token, base_url: str, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PUT request to a specified API
    - this is for internal use - you should use an API-specific `put` function instead

    Parameters
    ----------
    token: Token
        - authentication token

    base_url: str
        - base URL of desired API
        - must match your token's audience
        - valid: `URL_CORE`, `URL_LIVE`, `URL_MEET`, `URL_OAUTH`

    endpoint: str
        - desired endpoint or full URL
        - base URL and leading slash (`'https://.../'`) optional

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated
        - default: `{}` (empty)

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return _request(token, base_url, endpoint, params, 'put', body)


def _request(token: Token, base_url: str, endpoint: str, params: dict = {}, method: str = 'get', body: dict = {}) -> dict | list:
    '''
    - sends a request to a specified API
    - this is for internal use - you should use an explicit function like `core.get()` instead

    Parameters
    ----------
    token: Token
        - authentication token

    base_url: str
        - base URL of desired API
        - must match your token's audience
        - valid: `URL_CORE`, `URL_LIVE`, `URL_MEET`, `URL_OAUTH`

    endpoint: str
        - desired endpoint or full URL
        - base URL and leading slash (`'https://.../'`) optional

    params: dict
        - parameters for request if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated
        - default: `{}` (empty)

    method: str
        - type of request to send
        - valid: `'delete'`, `'get'`, `'head'`, `'options'`, `'patch'`, `'post'`, `'put'`
        - default: `'get'`

    body: dict
        - request body
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    util._log(f'{method.upper()} {base_url}/{endpoint} | params: {params} | body: {body}')

    if (base_url := base_url.lower()) not in (URL_CORE, URL_LIVE, URL_MEET, URL_OAUTH):
        raise ValueError(f'invalid base URL: {base_url}')

    if (method := method.lower()) not in ('delete', 'get', 'head', 'options', 'patch', 'post', 'put'):
        raise ValueError(f'invalid method: {method}')

    base_name: str = 'Core'

    if base_url == URL_CORE:
        if token.audience != AUDIENCE_CORE:
            raise ValueError(f'mismatched audience and base URL: {token.audience} | {base_url}')

    elif base_url in (URL_LIVE, URL_MEET):
        if token.audience != AUDIENCE_LIVE:
            raise ValueError(f'mismatched audience and base URL: {token.audience} | {base_url}')

        base_name = 'Live' if base_url == URL_LIVE else 'Meet'

    else:
        if token.audience != AUDIENCE_OAUTH:
            raise ValueError(f'mismatched audience and base URL: {token.audience} | {base_url}')

        base_name = AUDIENCE_OAUTH

    if token.expired:
        if issubclass(token, WebServicesToken):
            token.refresh()
        else:
            raise ValueError('OAuth2 token is expired and cannot be refreshed')

    if endpoint.startswith(base_url):
        endpoint = endpoint.split(base_url)[1]

    if endpoint.startswith('/'):
        endpoint = endpoint[1:]

    def __request() -> requests.Response:
        _wait()
        return getattr(requests, method)(  # trust that requests never breaks this
            url=f'{base_url}/{endpoint}',
            params=params,
            headers={'Authorization': token.access_token},
            json=body
        )

    req: requests.Response = __request()

    if req.status_code == 401:  # token may have expired prematurely
        if issubclass(token, WebServicesToken):
            token.refresh()
        else:
            raise ValueError('OAuth2 token is expired and cannot be refreshed')

        req = __request()

    if req.status_code >= 400:
        raise ConnectionError(f'bad response from {base_name} API: code {req.status_code}, response {req.text}')

    return req.json()


def _wait() -> None:
    now: int = util.stamp(True)
    if now - config._last_request_timestamp < config.wait_between_requests_ms:
        util._log('waiting to send next request')
        time.sleep(float(config._last_request_timestamp + config.wait_between_requests_ms - now) / 1000.0)
        config._last_request_timestamp = util.stamp(True)
    else:
        config._last_request_timestamp = now
