'''
- Tests for nadeo_api.oauth
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import src.nadeo_api.auth as auth
import src.nadeo_api.config as config
import src.nadeo_api.oauth as oauth


def get_account_ids_from_names(token: auth.OAuthToken) -> dict:
    return oauth.get_account_ids_from_names(token, ('Ezio.TM',))


def get_account_names_from_ids(token: auth.OAuthToken) -> dict:
    return oauth.get_account_names_from_ids(token, ('594be80b-62f3-4705-932b-e743e97882cf',))


def main() -> None:
    config.debug_logging = True

    token = auth.OAuthToken.get(
        os.environ['TM_OAUTH_IDENTIFIER'],
        os.environ['TM_OAUTH_SECRET']
    )
    assert token.access_token.token

    account_ids = get_account_ids_from_names(token)
    assert account_ids

    account_names = get_account_names_from_ids(token)
    assert account_names

    pass


if __name__ == '__main__':
    main()
