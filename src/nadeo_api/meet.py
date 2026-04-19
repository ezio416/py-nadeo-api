'''
- Functions for interacting with the web services Meet API
'''

from . import auth


AUDIENCE: str = auth.AUDIENCE_LIVE
URL:      str = auth.URL_MEET


######################################################### BASE #########################################################


def delete(token: auth.WebServicesToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a DELETE request to the Meet API

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

    return auth._delete(token, URL, endpoint, params, body)


def get(token: auth.WebServicesToken, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a GET request to the Meet API

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
    - sends a HEAD request to the Meet API

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
    - sends an OPTIONS request to the Meet API

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
    - sends a PATCH request to the Meet API

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
    - sends a POST request to the Meet API

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
    - sends a PUT request to the Meet API

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


def get_current_cotd(token: auth.WebServicesToken) -> dict:
    '''
    - gets info on the current cross-platform Cup of the Day
    - https://webservices.openplanet.dev/meet/competitions/current-cotd

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    Returns
    -------
    dict
        - Cup of the Day info
    '''

    return get(token, 'api/cup-of-the-day/current')


def get_matchmaking_divisions(token: auth.WebServicesToken, matchmaking_type: int | str) -> dict:
    '''
    - gets the available matchmaking divisions for a certain type
    - https://webservices.openplanet.dev/meet/matchmaking/divisions

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    matchmaking_type: int | str
        - either the ID or name for the type of matchmaking requested

    Returns
    -------
    dict
        - Cup of the Day info
    '''

    return get(token, f'api/matchmaking/{matchmaking_type}/division/display-rules')


def get_matchmaking_ids(token: auth.WebServicesToken) -> dict:
    '''
    - gets the available IDs for matchmaking
    - as of July 2025, this may return outdated information
    - https://webservices.openplanet.dev/meet/matchmaking/summary

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    Returns
    -------
    dict
        - matchmaking IDs
    '''

    return get(token, 'api/official/summary')


def get_matchmaking_player_status(token: auth.ServiceToken, matchmaking_type: int | str) -> dict:
    '''
    - gets the matchmaking status of the currently authenticated user
    - https://webservices.openplanet.dev/meet/matchmaking/player-status

    Parameters
    ----------
    token: auth.ServiceToken
        - authentication token

    matchmaking_type: int | str
        - either the ID or name for the type of matchmaking requested

    Returns
    -------
    dict
        - player matchmaking status
    '''

    auth.ServiceToken.check_type(token)

    return get(token, f'api/matchmaking/{matchmaking_type}/player-status')
