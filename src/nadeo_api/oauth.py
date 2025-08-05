'''
| Author:   Ezio416
| Created:  2024-05-15
| Modified: 2025-08-05

- Functions for interacting with the public Trackmania API
'''

import typing

from . import auth


AUDIENCE: str = auth.audience_oauth
URL:      str = auth.url_oauth


######################################################### BASE #########################################################


def delete(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a DELETE request to the OAuth2 API

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, i.e. `?param1=true&param2=0`

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._delete(token, URL, endpoint, params, body)


def get(token: auth.Token, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a GET request to the OAuth2 API

    Parameters
    ----------
    token: auth.Token
        - authentication token gotten from `auth.get_token`

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, i.e. `?param1=true&param2=0`

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here else they will be duplicated

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._get(token, URL, endpoint, params)


def head(token: auth.Token, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a HEAD request to the OAuth2 API

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, i.e. `?param1=true&param2=0`

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._head(token, URL, endpoint, params)


def options(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends an OPTIONS request to the OAuth2 API

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, i.e. `?param1=true&param2=0`

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._options(token, URL, endpoint, params, body)


def patch(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PATCH request to the OAuth2 API

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, i.e. `?param1=true&param2=0`

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._patch(token, URL, endpoint, params, body)


def post(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a POST request to the OAuth2 API

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, i.e. `?param1=true&param2=0`

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._post(token, URL, endpoint, params, body)


def put(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PUT request to the OAuth2 API

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    endpoint: str
        - desired endpoint
        - base URL is optional
        - leading forward slash is optional
        - trailing parameters are optional, i.e. `?param1=true&param2=0`

    params: dict
        - request parameters if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._put(token, URL, endpoint, params, body)


###################################################### ENDPOINTS #######################################################


def get_account_ids_from_names(token: auth.Token, account_names: typing.Iterable[str]) -> dict:
    '''
    - gets Ubisoft account IDs (UUID) given account names
    - https://webservices.openplanet.dev/oauth/reference/accounts/name-to-id

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    account_names: Iterable[str]
        - account names
        - if a name is not found, it will be omitted from the results

    Returns
    -------
    dict
        - returned account IDs as values with given account names as keys
    '''

    return get(token, f'api/display-names/account-ids?displayName[]={'&displayName[]='.join(account_names)}')


def get_account_names_from_ids(token: auth.Token, account_ids: typing.Iterable[str]) -> dict:
    '''
    - gets Ubisoft account names given account IDs (UUID)
    - https://webservices.openplanet.dev/oauth/reference/accounts/id-to-name

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    account_ids: str | Iterable[str]
        - account IDs (max 50)
        - raises a `ValueError` if you try to request more than 50 names
        - if an ID is not found, it will be omitted from the results

    Returns
    -------
    dict
        - returned account names as values with given account IDs as keys
    '''

    num_ids: int = len(account_ids)
    if num_ids > 50:
        raise ValueError(f'You can request a maximum of 50 account names. Requested: {num_ids}')

    return get(token, f'api/display-names?accountId[]={'&accountId[]='.join(account_ids)}')


###################################################### DEPRECATED ######################################################


def account_ids_from_names(token: auth.Token, account_names: str | typing.Iterable[str]) -> dict:
    '''
    - DEPRECATED - use `get_account_ids_from_names` instead
    '''

    if type(account_names) is str:
        return get_account_ids_from_names(token, [account_names])

    return get_account_ids_from_names(token, account_names)


def account_names_from_ids(token: auth.Token, account_ids: str | typing.Iterable[str]) -> dict:
    '''
    - DEPRECATED - use `get_account_names_from_ids` instead
    '''

    if type(account_ids) is str:
        return get_account_names_from_ids(token, [account_ids])

    return get_account_names_from_ids(token, account_ids)
