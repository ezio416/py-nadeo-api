'''
| Author:   Ezio416
| Created:  2024-05-15
| Modified: 2025-08-04

- Functions for interacting with the web services Meet API
'''

from . import auth


def delete(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a DELETE request to the Meet API

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
        - parameters for request if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._delete(token, auth.url_meet, endpoint, params, body)


def get(token: auth.Token, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a GET request to the Meet API

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
        - parameters for request if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._get(token, auth.url_meet, endpoint, params)


def head(token: auth.Token, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a HEAD request to the Meet API

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
        - parameters for request if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._head(token, auth.url_meet, endpoint, params)


def options(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends an OPTIONS request to the Meet API

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
        - parameters for request if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._options(token, auth.url_meet, endpoint, params, body)


def patch(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PATCH request to the Meet API

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
        - parameters for request if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._patch(token, auth.url_meet, endpoint, params, body)


def post(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a POST request to the Meet API

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
        - parameters for request if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._post(token, auth.url_meet, endpoint, params, body)


def put(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PUT request to the Meet API

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
        - parameters for request if applicable
        - if you put parameters at the end of the `endpoint`, do not put them here or they will be duplicated

    body: dict
        - request body if applicable
        - default: `{}` (empty)

    Returns
    -------
    dict | list
        - response body
    '''

    return auth._put(token, auth.url_meet, endpoint, params, body)


def current_cotd(token: auth.Token) -> dict:
    '''
    - gets info on the current cross-platform Cup of the Day
    - https://webservices.openplanet.dev/meet/cup-of-the-day/current

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    Returns
    -------
    dict
        - Cup of the Day info
    '''

    return get(token, 'api/cup-of-the-day/current')
