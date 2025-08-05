'''
| Author:   Ezio416
| Created:  2024-05-20
| Modified: 2025-08-04

- Various functions not directly related to any API
- You don't need to import this module - simply call these from the main module like `nadeo_api.<function>`
'''

import base64
import re


def account_id_from_login(account_login: str) -> str:
    '''
    - converts a base64-encoded login to a Ubisoft account ID (UUID)

    Parameters
    ----------
    account_login: str
        - base64-encoded login

    Returns
    -------
    str
        - account ID (UUID)
    '''

    if not bool(re.match('^[0-9A-Za-z\\-_]{22}$', account_login)):
        raise ValueError(f'Given account login is invalid: {account_login}')

    b: str = bytes.hex(base64.urlsafe_b64decode(f'{account_login}=='))

    return f'{b[:8]}-{b[8:12]}-{b[12:16]}-{b[16:20]}-{b[20:]}'


def account_login_from_id(account_id: str) -> str:
    '''
    - converts a Ubisoft account ID (UUID) to a base64-encoded login

    Parameters
    ----------
    account_id: str
        - account ID (UUID)

    Returns
    -------
    str
        - base64-encoded login
    '''

    if not valid_uuid(account_id):
        raise ValueError(f'Given account ID is invalid: {account_id}')

    return base64.urlsafe_b64encode(bytes.fromhex(account_id.replace('-', ''))).decode()[:-2]


def valid_uuid(uuid: str) -> bool:
    '''
    - checks if a given string looks like a valid UUID

    Parameters
    ----------
    uuid: str
        - string to check

    Returns
    -------
    bool
        - whether given string looks like a valid UUID
    '''

    return bool(re.match('^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$', uuid))
