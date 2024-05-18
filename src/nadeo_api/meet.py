'''
| Author:   Ezio416
| Created:  2024-05-15
| Modified: 2024-05-18

- Functions for interacting with the web services Meet API
'''

from . import auth


def get(token: auth.Token, endpoint: str, params: dict = {}) -> dict:
    '''
    - sends a GET request to the Meet API

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
        - parameters for request if applicable
        - if you specified parameters at the end of the `endpoint`, do not specify them here else they will be duplicated

    Returns
    -------
    dict
        - data returned from request
    '''

    return auth._get(token, auth.url_meet, endpoint, params)


def current_cotd(token: auth.Token) -> dict:
    '''
    - gets info on the current cross-platform Cup of the Day
    - https://webservices.openplanet.dev/meet/cup-of-the-day/current

    Parameters
    ----------
    token: auth.Token
        - authentication token gotten from `auth.get_token`

    Returns
    -------
    dict
        - Cup of the Day info
    '''

    return get(token, 'api/cup-of-the-day/current')
