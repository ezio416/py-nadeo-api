'''
| Author:   Ezio416
| Created:  2024-05-15
| Modified: 2025-08-05

- Functions for interacting with the web services Live API
'''

from . import auth


AUDIENCE: str = auth.audience_live
URL:      str = auth.url_live


######################################################### BASE #########################################################


def delete(token: auth.Token, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a DELETE request to the Live API

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
    - sends a GET request to the Live API

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
    - sends a HEAD request to the Live API

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
    - sends an OPTIONS request to the Live API

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
    - sends a PATCH request to the Live API

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
    - sends a POST request to the Live API

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
    - sends a PUT request to the Live API

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


def get_club_campaign(token: auth.Token, club_id: int, campaign_id: int) -> dict:
    '''
    - gets info on a campaign in a club
    - https://webservices.openplanet.dev/live/clubs/campaign-by-id

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    club_id: int
        - the ID of the club

    campaign_id: int
        - the ID of the campaign (not activity ID - campaign ID should be a lot smaller)

    Returns
    -------
    dict
        - info on campaign
    '''

    return get(token, f'api/token/club/{club_id}/campaign/{campaign_id}')


def get_map_leaderboard(token: auth.Token, mapUid: str, groupUid: str = 'Personal_Best', onlyWorld: bool = True, length: int = 5, offset: int = 0) -> dict:
    '''
    - gets the top leaderboard records for a map
    - can only retrieve records in the top 10,000
    - https://webservices.openplanet.dev/live/leaderboards/top

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    mapUid: str
        - the UID of the map

    groupUid: str
        - the UID of the group/season
        - default: `'Personal_Best'`

    onlyWorld: bool
        - whether to only get records from the global leaderboard
        - if `False`, a Ubisoft account is required and `length` and `offset` are ignored
        - default: `True`

    length: int
        - number of records to get (max 100)
        - default: `5`

    offset: int
        - number of records to skip
        - default: `0`
    '''

    if onlyWorld:
        if length > 100:
            raise ValueError('You can only request 100 records at a time')

        if length + offset > 10_000:
            raise ValueError('You can only retrieve records in the top 10,000')

        return get(token, f'api/token/leaderboard/group/{groupUid}/map/{mapUid}/top?onlyWorld=true&length={length}&offset={offset}')

    if token.server_account:
        raise ValueError('This endpoint requires a Ubisoft account when onlyWorld is False')

    return get(token, f'api/token/leaderboard/group/{groupUid}/map/{mapUid}/top?onlyWorld=false')


def get_maps_royal(token: auth.Token, length: int, offset: int = 0) -> dict:
    '''
    - gets Royal maps
    - note: no longer being updated so it's probably fine to cache this data permanently
    - https://webservices.openplanet.dev/live/campaigns/totds

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    length: int
        - number of months to get

    offset: int
        - number of months to skip, looking backwards from the current month
        - note: the last Royal maps are from June 2025, but this endpoint still looks back from the current month
        - default: `0`

    Returns
    -------
    dict
        - maps by month sorted newest to oldest
    '''

    return get(token, '/api/token/campaign/month', {'length': length, 'offset': offset, 'royal': 'true'})


def get_maps_seasonal(token: auth.Token, length: int, offset: int = 0) -> dict:
    '''
    - gets official Nadeo seasonal campaigns
    - https://webservices.openplanet.dev/live/campaigns/campaigns

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

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

    return get(token, 'api/campaign/official', {'length': length, 'offset': offset})


def get_maps_totd(token: auth.Token, length: int, offset: int = 0) -> dict:
    '''
    - gets Tracks of the Day
    - https://webservices.openplanet.dev/live/campaigns/totds

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

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


def get_maps_weekly(token: auth.Token, length: int, offset: int = 0) -> dict:
    '''
    - gets Weekly Shorts
    - https://webservices.openplanet.dev/live/campaigns/weekly-shorts

    Parameters
    ----------
    token: auth.Token
        - authentication token from `auth.get_token`

    length: int
        - number of weeks to get

    offset: int
        - number of weeks to skip, looking backwards from the current week
        - default: `0`

    Returns
    -------
    dict
        - maps by week sorted newest to oldest
    '''

    return get(token, '/api/campaign/weekly-shorts', {'length': length, 'offset': offset})


###################################################### DEPRECATED ######################################################


def maps_campaign(token: auth.Token, length: int, offset: int = 0) -> dict:
    '''
    - DEPRECATED - use `get_maps_seasonal` instead
    '''

    return get_maps_seasonal(token, length, offset)


def maps_royal(token: auth.Token, length: int, offset: int = 0) -> dict:
    '''
    - DEPRECATED - use `get_maps_royal` instead
    '''

    return get_maps_royal(token, length, offset)


def maps_totd(token: auth.Token, length: int, offset: int = 0) -> dict:
    '''
    - DEPRECATED - use `get_maps_totd` instead
    '''

    return get_maps_totd(token, length, offset)
