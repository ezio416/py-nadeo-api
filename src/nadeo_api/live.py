'''
- Functions for interacting with the web services Live API
'''

from . import auth


AUDIENCE: str = auth.AUDIENCE_LIVE
URL:      str = auth.URL_LIVE


######################################################### BASE #########################################################


def delete(token: auth.WebServicesToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a DELETE request to the Live API

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

    if not isinstance(token, auth.WebServicesToken):
        raise ValueError('web services endpoints require a web services token')

    return auth._delete(token, URL, endpoint, params, body)


def get(token: auth.WebServicesToken, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a GET request to the Live API

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

    if not isinstance(token, auth.WebServicesToken):
        raise ValueError('web services endpoints require a web services token')

    return auth._get(token, URL, endpoint, params)


def head(token: auth.WebServicesToken, endpoint: str, params: dict = {}) -> dict | list:
    '''
    - sends a HEAD request to the Live API

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

    if not isinstance(token, auth.WebServicesToken):
        raise ValueError('web services endpoints require a web services token')

    return auth._head(token, URL, endpoint, params)


def options(token: auth.WebServicesToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends an OPTIONS request to the Live API

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

    if not isinstance(token, auth.WebServicesToken):
        raise ValueError('web services endpoints require a web services token')

    return auth._options(token, URL, endpoint, params, body)


def patch(token: auth.WebServicesToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PATCH request to the Live API

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

    if not isinstance(token, auth.WebServicesToken):
        raise ValueError('web services endpoints require a web services token')

    return auth._patch(token, URL, endpoint, params, body)


def post(token: auth.WebServicesToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a POST request to the Live API

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

    if not isinstance(token, auth.WebServicesToken):
        raise ValueError('web services endpoints require a web services token')

    return auth._post(token, URL, endpoint, params, body)


def put(token: auth.WebServicesToken, endpoint: str, params: dict = {}, body: dict = {}) -> dict | list:
    '''
    - sends a PUT request to the Live API

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

    if not isinstance(token, auth.WebServicesToken):
        raise ValueError('web services endpoints require a web services token')

    return auth._put(token, URL, endpoint, params, body)


###################################################### ENDPOINTS #######################################################


def get_club_campaign(token: auth.WebServicesToken, club_id: int, campaign_id: int) -> dict:
    '''
    - gets info on a campaign in a club
    - https://webservices.openplanet.dev/live/clubs/campaign-by-id

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

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


def get_map_leaderboard(token: auth.WebServicesToken, mapUid: str, groupUid: str = 'Personal_Best', onlyWorld: bool = True, length: int = 5, offset: int = 0) -> dict:
    '''
    - gets the top leaderboard records for a map
    - can only retrieve records in the top 10,000
    - https://webservices.openplanet.dev/live/leaderboards/top

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    mapUid: str
        - the UID of the map

    groupUid: str
        - the UID of the group/season
        - default: `'Personal_Best'`

    onlyWorld: bool
        - whether to only get records from the global leaderboard
        - if `False`, a service account is required and `length` and `offset` are ignored
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
            raise ValueError('you can only request 100 records at a time')

        if length + offset > 10_000:
            raise ValueError('you can only retrieve records in the top 10,000')

        return get(token, f'api/token/leaderboard/group/{groupUid}/map/{mapUid}/top?onlyWorld=true&length={length}&offset={offset}')

    if not isinstance(token, auth.ServiceToken):
        raise ValueError('this endpoint requires a service account when onlyWorld is False')

    return get(token, f'api/token/leaderboard/group/{groupUid}/map/{mapUid}/top?onlyWorld=false')


def get_maps_royal(token: auth.WebServicesToken, length: int = 51, offset: int = 0) -> dict:
    '''
    - gets Royal maps
    - note: no longer being updated so it's probably fine to cache this data permanently
    - https://webservices.openplanet.dev/live/campaigns/totds

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    length: int
        - number of months to get
        - default: `51` (total released)

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


def get_maps_seasonal(token: auth.WebServicesToken, length: int = 1, offset: int = 0) -> dict:
    '''
    - gets official Nadeo seasonal campaigns
    - https://webservices.openplanet.dev/live/campaigns/campaigns-v2

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    length: int
        - number of campaigns to get
        - default: `1`

    offset: int
        - number of campaigns to skip, looking backwards from the current campaign
        - default: `0`

    Returns
    -------
    dict
        - campaigns sorted newest to oldest
    '''

    return get(token, 'api/campaign/official', {'length': length, 'offset': offset})


def get_maps_totd(token: auth.WebServicesToken, length: int = 1, offset: int = 0) -> dict:
    '''
    - gets Tracks of the Day
    - https://webservices.openplanet.dev/live/campaigns/totds

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    length: int
        - number of months to get
        - default: `1`

    offset: int
        - number of months to skip, looking backwards from the current month
        - default: `0`

    Returns
    -------
    dict
        - maps by month sorted newest to oldest
    '''

    return get(token, '/api/token/campaign/month', {'length': length, 'offset': offset})


def get_maps_weekly_grand(token: auth.WebServicesToken, length: int = 1, offset: int = 0) -> dict:
    '''
    - gets Weekly Grands
    - https://webservices.openplanet.dev/live/campaigns/weekly-grands

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    length: int
        - number of weeks to get
        - default: `1`

    offset: int
        - number of weeks to skip, looking backwards from the current week
        - default: `0`

    Returns
    -------
    dict
        - maps by week sorted newest to oldest
    '''

    return get(token, '/api/campaign/weekly-grands', {'length': length, 'offset': offset})


def get_maps_weekly_short(token: auth.WebServicesToken, length: int = 1, offset: int = 0) -> dict:
    '''
    - gets Weekly Shorts
    - https://webservices.openplanet.dev/live/campaigns/weekly-shorts

    Parameters
    ----------
    token: auth.WebServicesToken
        - authentication token

    length: int
        - number of weeks to get
        - default: `1`

    offset: int
        - number of weeks to skip, looking backwards from the current week
        - default: `0`

    Returns
    -------
    dict
        - maps by week sorted newest to oldest
    '''

    return get(token, '/api/campaign/weekly-shorts', {'length': length, 'offset': offset})
