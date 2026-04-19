'''
- Tests for nadeo_api.oauth
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import src.nadeo_api.auth as auth
import src.nadeo_api.config as config
import src.nadeo_api.oauth as oauth


def main() -> None:
    config.debug_logging = True

    token = auth.OAuthToken.get(
        os.environ['TM_OAUTH_IDENTIFIER'],
        os.environ['TM_OAUTH_SECRET']
    )
    assert token.access_token.token

    ...

    pass


if __name__ == '__main__':
    main()
