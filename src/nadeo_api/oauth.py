'''
- Functions for interacting with the public Trackmania API
'''

import typing

from . import auth
from . import error


AUDIENCE: str = auth.AUDIENCE_OAUTH
URL:      str = auth.URL_OAUTH


######################################################### BASE #########################################################


def delete(token: auth.OAuthToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a DELETE request to the OAuth2 API

    Parameters
    ----------
    token: auth.OAuthToken
        - authentication token

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, e.g. `?param1=true&param2=0`

    params: dict
        - request parameters, if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body, if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    auth.OAuthToken.check_type(token)

    return auth._delete(token, URL, endpoint, params, body)


def get(token: auth.OAuthToken, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a GET request to the OAuth2 API

    Parameters
    ----------
    token: auth.OAuthToken
        - authentication token

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, e.g. `?param1=true&param2=0`

    params: dict
        - request parameters, if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here else they will be duplicated

    Returns
    -------
    dict | list
        - response body
    '''

    auth.OAuthToken.check_type(token)

    return auth._get(token, URL, endpoint, params)


def head(token: auth.OAuthToken, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a HEAD request to the OAuth2 API

    Parameters
    ----------
    token: auth.OAuthToken
        - authentication token

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, e.g. `?param1=true&param2=0`

    params: dict
        - request parameters, if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    Returns
    -------
    dict | list
        - response body
    '''

    auth.OAuthToken.check_type(token)

    return auth._head(token, URL, endpoint, params)


def options(token: auth.OAuthToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends an OPTIONS request to the OAuth2 API

    Parameters
    ----------
    token: auth.OAuthToken
        - authentication token

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, e.g. `?param1=true&param2=0`

    params: dict
        - request parameters, if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body, if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    auth.OAuthToken.check_type(token)

    return auth._options(token, URL, endpoint, params, body)


def patch(token: auth.OAuthToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PATCH request to the OAuth2 API

    Parameters
    ----------
    token: auth.OAuthToken
        - authentication token

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, e.g. `?param1=true&param2=0`

    params: dict
        - request parameters, if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body, if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    auth.OAuthToken.check_type(token)

    return auth._patch(token, URL, endpoint, params, body)


def post(token: auth.OAuthToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a POST request to the OAuth2 API

    Parameters
    ----------
    token: auth.OAuthToken
        - authentication token

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, e.g. `?param1=true&param2=0`

    params: dict
        - request parameters, if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body, if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    auth.OAuthToken.check_type(token)

    return auth._post(token, URL, endpoint, params, body)


def put(token: auth.OAuthToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PUT request to the OAuth2 API

    Parameters
    ----------
    token: auth.OAuthToken
        - authentication token

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, e.g. `?param1=true&param2=0`

    params: dict
        - request parameters, if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body, if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    auth.OAuthToken.check_type(token)

    return auth._put(token, URL, endpoint, params, body)


###################################################### ENDPOINTS #######################################################


def get_account_ids_from_names(token: auth.OAuthToken, account_names: typing.Iterable[str]) -> dict:
    '''
    - gets Ubisoft account IDs (UUID) given account names
    - https://webservices.openplanet.dev/oauth/reference/accounts/name-to-id

    Parameters
    ----------
    token: auth.OAuthToken
        - authentication token

    account_names: Iterable[str]
        - account names
        - if a name is not found, it will be omitted from the results

    Returns
    -------
    dict
        - returned account IDs as values with given account names as keys
    '''

    return get(token, f'api/display-names/account-ids?displayName[]={'&displayName[]='.join(account_names)}')


def get_account_names_from_ids(token: auth.OAuthToken, account_ids: typing.Iterable[str]) -> dict:
    '''
    - gets Ubisoft account names given account IDs (UUID)
    - https://webservices.openplanet.dev/oauth/reference/accounts/id-to-name

    Parameters
    ----------
    token: auth.OAuthToken
        - authentication token

    account_ids: Iterable[str]
        - account IDs (max 50)
        - if an ID is not found, it will be omitted from the results

    Returns
    -------
    dict
        - returned account names as values with given account IDs as keys
    '''

    if (num_ids := len(account_ids)) > 50:
        raise error.ParameterError(f'you can request a maximum of 50 account names, not: {num_ids}')

    return get(token, f'api/display-names?accountId[]={'&accountId[]='.join(account_ids)}')
