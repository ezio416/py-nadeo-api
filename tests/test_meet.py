'''
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

    token_dedi = auth.DedicatedServerToken.get(
        meet.AUDIENCE,
        os.environ['TM_E416DEV_SERVER_USERNAME'],
        os.environ['TM_E416DEV_SERVER_PASSWORD'],
        os.environ['TM_E416DEV_AGENT']
    )
    assert token_dedi.access_token.token

    token_service = auth.ServiceToken.get(
        meet.AUDIENCE,
        os.environ['TM_SERVICE_USERNAME'],
        os.environ['TM_SERVICE_PASSWORD'],
        os.environ['TM_E416DEV_AGENT']
    )
    assert token_service.access_token.token

    ...

    pass


if __name__ == '__main__':
    main()
