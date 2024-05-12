'''
| Author:   Ezio416
| Created:  2024-05-07
| Modified: 2024-05-12

- Functions for interacting with authentication tokens to use with the API
'''

from base64 import b64encode, urlsafe_b64decode
from dataclasses import dataclass
from datetime import datetime as dt
from json import loads
import time

from requests import post


audience_core:  str = 'NadeoServices'
audience_live:  str = 'NadeoLiveServices'  # also used for 'meet' endpoints (formerly known as club)
audience_oauth: str = 'OAuth2'
tmnext_app_id:  str = '86263886-327a-4328-ac69-527f0d20a237'
url_core:       str = 'https://prod.trackmania.core.nadeo.online'
url_live:       str = 'https://live-services.trackmania.nadeo.live'
url_meet:       str = 'https://meet.trackmania.nadeo.club'


@dataclass
class Token():
    '''
    - holds data on an authentication token

    Parameters
    ----------
    access_token: str
        - access token/ticket

    audience: str
        - audience for which token is valid

    refresh_token: str
        - token used to refresh access token if applicable
        - default: `''` (empty)

    server_account: bool
        - whether the token is for a dedicated server account instead of a Ubisoft account
        - default: `False`

    expiration: int
        - time at which access token/ticket will expire
        - if not given, will be decoded from the token's payload
        - default: `0`
    '''

    access_token:   str
    audience:       str
    expiration:     int
    refresh_token:  str
    server_account: bool
    token_decoded:  dict

    def __init__(self, access_token: str, audience: str, refresh_token: str = '', server_account: bool = False, expiration: int = 0):
        self.access_token   = access_token
        self.audience       = audience
        self.refresh_token  = refresh_token
        self.server_account = server_account

        try:  # will fail if passed a ticket (not a JWT) instead of a token
            self.token_decoded  = loads(urlsafe_b64decode(f'{self.access_token.split('.')[1]}==').decode('utf-8'))
        except UnicodeDecodeError as e:
            pass

        if expiration != 0:
            self.expiration = expiration
        else:
            try:
                self.expiration = self.token_decoded['exp']
            except Exception as e:
                self.expiration = int(time.time()) + 3600

    def __repr__(self) -> str:
        return f"nadeo_api.auth.Token('{self.audience}')"

    def __str__(self) -> str:
        return self.access_token

    @property
    def expired(self) -> bool:
        return int(time.time()) >= self.expiration

    def refresh(self) -> None:
        pass


def get_token(audience: str, agent: str, username: str, password: str, server_account: bool = False) -> Token:
    '''
    - requests an authentication token for a given audience

    Parameters
    ----------
    audience: str
        - desired audience for token use
        - capitalization is ignored
        - valid: `NadeoServices`/`core`/`prod`, `NadeoLiveServices`/`live`/`meet`/`club`, `OAuth`/`OAuth2`

    agent: str
        - user agent, ideally with your program's name and a way to contact you
        - Ubisoft can block you without this being properly set

    username: str
        - Ubisoft/dedicated server account username
        - for OAuth, this is the identifier

    password: str
        - Ubisoft/dedicated server account password
        - for OAuth, this is the secret

    server_account: bool
        - whether you're using a dedicated server account instead of a Ubisoft account
        - default: `False`
    '''

    aud_lower: str = audience.lower()

    if aud_lower in ('nadeoservices', 'core', 'prod'):
        audience = audience_core
    elif aud_lower in ('nadeoliveservices', 'live', 'meet', 'club'):
        audience = audience_live
    elif aud_lower in ('oauth', 'oauth2'):
        audience = audience_oauth
    else:
        raise ValueError(f'Given audience is not valid: {audience}')

    if audience == audience_oauth:
        req = post(
            'https://api.trackmania.com/api/access_token',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data={
                'grant_type':    'client_credentials',
                'client_id':     username,
                'client_secret': password
            }
        )

        if req.status_code >= 400:
            raise ConnectionError(f'Bad response getting token for {audience}: code {req.status_code}, response {req.text}')

        json: dict = req.json()
        return Token(json['access_token'], audience, expiration=int(time.time()) + json['expires_in'])

    req = post(
        f'{url_core}/v2/authentication/token/basic' if server_account else 'https://public-ubiservices.ubi.com/v3/profiles/sessions',
        headers={
            'Authorization': f'Basic {b64encode(f'{username}:{password}'.encode('utf-8')).decode('ascii')}',
            'Content-Type':  'application/json',
            'Ubi-AppId':     tmnext_app_id,
            'User-Agent':    agent,
        },
        json={'audience': audience}
    )

    if req.status_code >= 400:
        raise ConnectionError(f'Bad response getting ticket for {audience}: code {req.status_code}, response {req.text}')

    json: dict = req.json()

    if server_account:
        return Token(f'nadeo_v1 t={json['accessToken']}', audience, f'nadeo_v1 t={json['refreshToken']}', True)

    ticket: Token = Token(f'ubi_v1 t={json['ticket']}', json['platformType'], expiration=int(dt.fromisoformat(json['expiration']).timestamp()))

    req2 = post(
        f'{url_core}/v2/authentication/token/ubiservices',
        headers={'Authorization': ticket.access_token},
        json={'audience': audience}
    )

    if req2.status_code >= 400:
        raise ConnectionError(f'Bad response getting token for {audience}: code {req.status_code}, response {req.text}')

    json2: dict = req2.json()
    return Token(f'nadeo_v1 t={json2['accessToken']}', audience, f'nadeo_v1 t={json2['refreshToken']}')
