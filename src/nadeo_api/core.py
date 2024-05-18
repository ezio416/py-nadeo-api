'''
| Author:   Ezio416
| Created:  2024-05-14
| Modified: 2024-05-18

- Functions for interacting with the web services Core API
'''

from . import auth


def get(token: auth.Token, endpoint: str, params: dict = {}) -> dict:
    '''
    - sends a GET request to the Core API

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

    return auth._get(token, auth.url_core, endpoint, params)


def routes(token: auth.Token, usage: str = 'Client') -> dict:
    '''
    - gets the valid Core API routes
    - https://webservices.openplanet.dev/core/meta/routes

    Parameters
    ----------
    token: auth.Token
        - authentication token gotten from `auth.get_token`

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


def zones(token: auth.Token) -> dict:
    '''
    - gets the valid regions a player may choose from
    - https://webservices.openplanet.dev/core/meta/zones

    Parameters
    ----------
    token: auth.Token
        - authentication token gotten from `auth.get_token`

    Returns
    -------
    dict
        - zones sorted alphabetically
    '''

    return get(token, 'zones')
