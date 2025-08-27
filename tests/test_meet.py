'''
| Author:   Ezio416
| Created:  2025-08-04
| Modified: 2025-08-26

- Tests for nadeo_api.meet
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import src.nadeo_api.auth as auth
import src.nadeo_api.config as config
import src.nadeo_api.meet as meet


def main() -> None:
    config.debug_logging = True

    token: auth.Token = auth.get_token(
        'meet',
        os.environ['TM_E416DEV_SERVER_USERNAME'],
        os.environ['TM_E416DEV_SERVER_PASSWORD'],
        os.environ['TM_E416DEV_AGENT'],
        True
    )

    # req = meet.get_matchmaking_ids(token)

    pass


if __name__ == '__main__':
    main()
