'''
- Functions for interacting with the web services Core API
'''

import typing

from . import auth
from . import error
from . import util


AUDIENCE: str = auth.AUDIENCE_CORE
URL:      str = auth.URL_CORE


######################################################### BASE #########################################################


def delete(token: auth.WebServicesToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a DELETE request to the Core API

    Parameters
    ----------
    token: auth.WebServicesToken
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
        - request body if, applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    auth.WebServicesToken.check_type(token)
    token.check_audience(AUDIENCE)

    return auth._delete(token, URL, endpoint, params, body)


def get(token: auth.WebServicesToken, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a GET request to the Core API

    Parameters
    ----------
    token: auth.WebServicesToken
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

    auth.WebServicesToken.check_type(token)
    token.check_audience(AUDIENCE)

    return auth._get(token, URL, endpoint, params)


def head(token: auth.WebServicesToken, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a HEAD request to the Core API

    Parameters
    ----------
    token: auth.WebServicesToken
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

    auth.WebServicesToken.check_type(token)
    token.check_audience(AUDIENCE)

    return auth._head(token, URL, endpoint, params)


def options(token: auth.WebServicesToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends an OPTIONS request to the Core API

    Parameters
    ----------
    token: auth.WebServicesToken
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

    auth.WebServicesToken.check_type(token)
    token.check_audience(AUDIENCE)

    return auth._options(token, URL, endpoint, params, body)


def patch(token: auth.WebServicesToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PATCH request to the Core API

    Parameters
    ----------
    token: auth.WebServicesToken
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

    auth.WebServicesToken.check_type(token)
    token.check_audience(AUDIENCE)

    return auth._patch(token, URL, endpoint, params, body)


def post(token: auth.WebServicesToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a POST request to the Core API

    Parameters
    ----------
    token: auth.WebServicesToken
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

    auth.WebServicesToken.check_type(token)
    token.check_audience(AUDIENCE)

    return auth._post(token, URL, endpoint, params, body)


def put(token: auth.WebServicesToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PUT request to the Core API

    Parameters
    ----------
    token: auth.WebServicesToken
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

    auth.WebServicesToken.check_type(token)
    token.check_audience(AUDIENCE)

    return auth._put(token, URL, endpoint, params, body)


###################################################### ENDPOINTS #######################################################


def get_map_info(token: auth.WebServicesToken, uids: typing.Iterable[str]) -> list[dict]:
    '''
    - gets info on multiple maps from their UIDs
    - https://webservices.openplanet.dev/core/maps/info-multiple-uid

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    uids: Iterable[str]
        - map UIDs

    Returns
    -------
    list[dict]
        - map info
    '''

    UID_LIMIT: int = 291

    if len(uids) <= UID_LIMIT:
        return get(token, f'maps/by-uid/?mapUidList={','.join(uids)}')

    ret: list[dict] = []

    while len(uids):
        uid_count: int = min(len(uids), UID_LIMIT)
        uids_this_req: list[str] = uids[:uid_count]
        uids = uids[uid_count:]
        endpoint: str = f'maps/by-uid/?mapUidList={','.join(uids_this_req)}'

        req: list[dict] = get(token, endpoint)
        for map in req:
            ret.append(map)

    return ret


def get_routes(token: auth.WebServicesToken, usage: str = 'Client') -> dict:
    '''
    - gets the valid Core API routes
    - https://webservices.openplanet.dev/core/meta/routes

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    usage: str
        - which authorization type to get routes for
        - `'Client'` is for a Ubisoft/service account, while `'Server'` is for a dedicated server account
        - valid: `'Client'`, `'Server'`
        - default: `'Client'`

    Returns
    -------
    dict
        - valid routes for given usage
    '''

    if usage not in ('Client', 'Server'):
        raise error.ParameterError(f'invalid usage: {usage}')

    return get(token, 'api/routes', {'usage': usage})


def get_trophies_history(token: auth.ServiceToken, account_id: str = '', count: int = 100, offset: int = 0) -> dict:
    '''
    - gets a list of trophy gain history
    - https://webservices.openplanet.dev/core/accounts/trophy-history

    Parameters
    ----------
    token: auth.ServiceToken
        - authentication token

    account_id: str
        - account ID to get data for
        - may be a different ID to the one being used for authentication
        - if not given, the currently authenticated account will be used
        - default: `''` (empty)

    count: int
        - number of history entries to get
        - if you set this too high, the request may time out (response 504)
        - maximum: `1,000`
        - default: `100`

    offset: int
        - number of history entries to skip, looking backwards from the most recent
        - default: 0

    Returns
    -------
    dict
        - history entries sorted newest to oldest
    '''

    auth.ServiceToken.check_type(token)

    if account_id and not util.valid_uuid(account_id):
        raise error.ParameterError(f'invalid account ID: {account_id}')

    if not account_id:
        account_id = token.account_id

    if count > 1_000:
        raise error.ParameterError('you can only request 1,000 history entries at a time')

    return get(token, f'accounts/{account_id}/trophies', {'count': count, 'offset': offset})


def get_trophies_last_year_summary(token: auth.ServiceToken, account_id: str = '') -> dict:
    '''
    - gets a summary of the trophies gained in the last year
    - https://webservices.openplanet.dev/core/accounts/trophy-summary

    Parameters
    ----------
    token: auth.ServiceToken
        - authentication token

    account_id: str
        - account ID to get data for
        - may be a different ID to the one being used for authentication
        - if not given, the currently authenticated account will be used
        - default: `''` (empty)

    Returns
    -------
    dict
        - data on given account
    '''

    auth.ServiceToken.check_type(token)

    if account_id and not util.valid_uuid(account_id):
        raise error.ParameterError(f'invalid account ID: {account_id}')

    if not account_id:
        account_id = token.account_id

    return get(token, f'accounts/{account_id}/trophies/lastYearSummary')


def get_zones(token: auth.WebServicesToken) -> list[dict]:
    '''
    - gets the valid regions a player may choose from
    - https://webservices.openplanet.dev/core/meta/zones

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    Returns
    -------
    list[dict]
        - zones sorted alphabetically by name
    '''

    return get(token, 'zones')
