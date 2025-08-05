'''
| Author:   Ezio416
| Created:  2025-08-04
| Modified: 2025-08-05

- Tests for nadeo_api.meet
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import src.nadeo_api.auth as auth
import src.nadeo_api.meet as meet
import src.nadeo_api.state as state


def main() -> None:
    token: auth.Token = auth.get_token(
        'meet',
        os.environ['TM_E416DEV_SERVER_USERNAME'],
        os.environ['TM_E416DEV_SERVER_PASSWORD'],
        os.environ['TM_E416DEV_AGENT'],
        True
    )

    state.debug_logging = True

    pass


if __name__ == '__main__':
    main()
