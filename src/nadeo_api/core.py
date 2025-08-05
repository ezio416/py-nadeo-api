'''
| Author:   Ezio416
| Created:  2024-05-14
| Modified: 2025-08-05

- Functions for interacting with the web services Core API
'''

import typing

from . import auth
from . import util


AUDIENCE: str = auth.audience_core
URL:      str = auth.url_core


######################################################### BASE #########################################################


def delete(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a DELETE request to the Core API

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
    - sends a GET request to the Core API

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

    return auth._get(token, URL, endpoint, params)


def head(token: auth.Token, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a HEAD request to the Core API

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
    - sends an OPTIONS request to the Core API

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
    - sends a PATCH request to the Core API

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
    - sends a POST request to the Core API

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
    - sends a PUT request to the Core API

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


def get_map_info(token: auth.Token, uids: typing.Iterable[str]) -> list[dict]:
    '''
    - gets info on multiple maps from their UIDs

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    uids: Iterable[str]
        - map UIDs

    Returns
    -------
    list[dict]
        - map info
    '''

    UID_LIMIT: int = 291

    if len(uids) <= UID_LIMIT:
        return get(token, f'maps/?mapUidList={','.join(uids)}')

    ret: list[dict] = []

    while len(uids):
        uid_count: int = min(len(uids), UID_LIMIT)
        uids_this_req: list[str] = uids[:uid_count]
        uids = uids[uid_count:]
        endpoint: str = f'maps/?mapUidList={','.join(uids_this_req)}'

        req: list[dict] = get(token, endpoint)
        for map in req:
            ret.append(map)

    return ret


def get_routes(token: auth.Token, usage: str = 'Client') -> dict:
    '''
    - gets the valid Core API routes
    - https://webservices.openplanet.dev/core/meta/routes

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    usage: str
        - which authorization type to get routes for
        - `'Client'` is for an Ubisoft account, while `'Server'` is for a dedicated server account
        - valid: `'Client'`, `'Server'`
        - default: `'Client'`

    Returns
    -------
    dict
        - valid routes for given usage
    '''

    if usage not in ('Client', 'Server'):
        raise ValueError(f'Given usage is invalid: {usage}')

    return get(token, 'api/routes', {'usage': usage})


def get_trophies_history(token: auth.Token, account_id: str, count: int, offset: int = 0) -> dict:
    '''
    - gets a list of trophy gain history
    - requires a Ubisoft account (client usage)

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    account_id: str
        - account ID to get data for

    count: int
        - number of history entries to get
        - if you set this too high, the request may time out (response 504)

    offset: int
        - number of history entries to skip, looking backwards from the most recent
        - default: 0

    Returns
    -------
    dict
        - history entries sorted newest to oldest
    '''

    if not util.valid_uuid(account_id):
        raise ValueError(f'Given account ID is invalid: {account_id}')

    if token.server_account:
        raise ValueError('This endpoint requires a Ubisoft account (client usage)')

    return get(token, f'accounts/{account_id}/trophies', {'offset': offset, 'count': count})


def get_trophies_last_year_summary(token: auth.Token, account_id: str) -> dict:
    '''
    - gets a summary of the trophies gained in the last year
    - requires a Ubisoft account (client usage)

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    account_id: str
        - account ID to get data for

    Returns
    -------
    dict
        - data on given account
    '''

    if not util.valid_uuid(account_id):
        raise ValueError(f'Given account ID is invalid: {account_id}')

    if token.server_account:
        raise ValueError('This endpoint requires a Ubisoft account (client usage)')

    return get(token, f'accounts/{account_id}/trophies/lastYearSummary')


def get_zones(token: auth.Token) -> list[dict]:
    '''
    - gets the valid regions a player may choose from
    - https://webservices.openplanet.dev/core/meta/zones

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    Returns
    -------
    list[dict]
        - zones sorted alphabetically by name
    '''

    return get(token, 'zones')


###################################################### DEPRECATED ######################################################


def routes(token: auth.Token, usage: str = 'Client') -> dict:
    '''
    - DEPRECATED - use `get_routes` instead
    '''

    return get_routes(token, usage)


def trophies_history(token: auth.Token, account_id: str, count: int, offset: int = 0) -> dict:
    '''
    - DEPRECATED - use `get_trophies_history` instead
    '''

    return get_trophies_history(token, account_id, count, offset)


def trophies_last_year_summary(token: auth.Token, account_id: str) -> dict:
    '''
    - DEPRECATED - use `get_trophies_last_year_summary` instead
    '''

    return get_trophies_last_year_summary(token, account_id)


def zones(token: auth.Token) -> list[dict]:
    '''
    - DEPRECATED - use `get_zones` instead
    '''

    return get_zones(token)
