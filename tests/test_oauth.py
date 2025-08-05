'''
| Author:   Ezio416
| Created:  2025-08-04
| Modified: 2025-08-05

- Tests for nadeo_api.oauth
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import src.nadeo_api.auth as auth
import src.nadeo_api.config as config
import src.nadeo_api.oauth as oauth


def main() -> None:
    token: auth.Token = auth.get_token(
        auth.audience_oauth,
        os.environ['TM_OAUTH_IDENTIFIER'],
        os.environ['TM_OAUTH_SECRET']
    )

    config.debug_logging = True

    pass


if __name__ == '__main__':
    main()
