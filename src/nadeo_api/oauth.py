'''
| Author:   Ezio416
| Created:  2024-05-15
| Modified: 2024-05-18

- Functions for interacting with the public Trackmania API
'''

from typing import Iterable

from . import auth


def get(token: auth.Token, endpoint: str, params: dict = {}) -> dict:
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
        - parameters for request if applicable
        - if you specified parameters at the end of the `endpoint`, do not specify them here else they will be duplicated

    Returns
    -------
    dict
        - data returned from request
    '''

    return auth._get(token, auth.url_oauth, endpoint, params)


def account_names_from_ids(token: auth.Token, account_ids: str | Iterable[str]) -> dict:
    '''
    - gets Ubisoft account names given account IDs (UUID)
    - https://webservices.openplanet.dev/oauth/reference/accounts/id-to-name

    Parameters
    ----------
    token: auth.Token
        - authentication token gotten from `auth.get_token`

    account_ids: str | Iterable[str]
        - account ID
        - may be an iterable of account IDs (max 50)
        - raises a `ValueError` if you try to request more than 50 names
        - if an ID is not found, it will be omitted from the results

    Returns
    -------
    dict
        - returned account names as values with given account IDs as keys
    '''

    if type(account_ids) is str:
        return get(token, 'api/display-names', {'accountId[]': account_ids})

    num_ids: int = len(account_ids)
    if num_ids > 50:
        raise ValueError(f'You can request a maximum of 50 account names. Requested: {num_ids}')

    return get(token, f'api/display-names?accountId[]={'&accountId[]='.join(account_ids)}')


def account_ids_from_names(token: auth.Token, account_names: str | Iterable[str]) -> dict:
    '''
    - gets Ubisoft account IDs (UUID) given account names
    - https://webservices.openplanet.dev/oauth/reference/accounts/name-to-id

    Parameters
    ----------
    token: auth.Token
        - authentication token gotten from `auth.get_token`

    account_name: str | Iterable[str]
        - account name
        - may be an iterable of account names
        - if a name is not found, it will be omitted from the results

    Returns
    -------
    dict
        - returned account IDs as values with given account names as keys
    '''

    if type(account_names) is str:
        return get(token, 'api/display-names/account-ids', {'displayName[]': account_names})

    return get(token, f'api/display-names/account-ids?displayName[]={'&displayName[]='.join(account_names)}')
