'''
| Author:   Ezio416
| Created:  2024-05-07
| Modified: 2024-05-19

- A library to assist with accessing Nadeo's web services API and the public Trackmania API (OAuth2).
- This is the main module - most of what you need is in sub-modules.
'''

import base64
import re


__version__: tuple = 0, 4.0


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
        - account ID
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

    if not bool(re.match('^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$', account_id)):
        raise ValueError(f'Given account ID is not a valid UUID: {account_id}')

    return base64.urlsafe_b64encode(bytes.fromhex(account_id.replace('-', ''))).decode()[:-2]
