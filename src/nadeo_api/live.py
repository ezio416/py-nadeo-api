'''
| Author:   Ezio416
| Created:  2024-05-15
| Modified: 2024-05-18

- Functions for interacting with the web services Live API
'''

from . import auth


def get(token: auth.Token, endpoint: str, params: dict = {}) -> dict:
    '''
    - sends a GET request to the Live API

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

    return auth._get(token, auth.url_live, endpoint, params)


def maps_campaign(token: auth.Token, length: int, offset: int = 0) -> dict:
    '''
    - gets official Nadeo seasonal campaigns
    - https://webservices.openplanet.dev/live/campaigns/campaigns

    Parameters
    ----------
    token: auth.Token
        - authentication token gotten from `auth.get_token`

    length: int
        - number of campaigns to get

    offset: int
        - number of campaigns to skip, looking backwards from the current campaign
        - default: `0`

    Returns
    -------
    dict
        - campaigns sorted newest to oldest
    '''

    return get(token, 'api/token/campaign/official', {'length': length, 'offset': offset})


def maps_royal(token: auth.Token, length: int, offset: int = 0) -> dict:
    '''
    - gets Royal maps
    - https://webservices.openplanet.dev/live/campaigns/totds

    Parameters
    ----------
    token: auth.Token
        - authentication token gotten from `auth.get_token`

    length: int
        - number of months to get

    offset: int
        - number of months to skip, looking backwards from the current month
        - default: `0`

    Returns
    -------
    dict
        - maps by month sorted newest to oldest
    '''

    return get(token, '/api/token/campaign/month', {'length': length, 'offset': offset, 'royal': 'true'})


def maps_totd(token: auth.Token, length: int, offset: int = 0) -> dict:
    '''
    - gets Tracks of the Day
    - https://webservices.openplanet.dev/live/campaigns/totds

    Parameters
    ----------
    token: auth.Token
        - authentication token gotten from `auth.get_token`

    length: int
        - number of months to get

    offset: int
        - number of months to skip, looking backwards from the current month
        - default: `0`

    Returns
    -------
    dict
        - maps by month sorted newest to oldest
    '''

    return get(token, '/api/token/campaign/month', {'length': length, 'offset': offset})
