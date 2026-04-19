'''
- Tests for nadeo_api.auth
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import src.nadeo_api.auth as auth
import src.nadeo_api.config as config


def main() -> None:
    config.debug_logging = True

    token_dedi_core = auth.DedicatedServerToken.get(
        auth.AUDIENCE_CORE,
        os.environ['TM_E416DEV_SERVER_USERNAME'],
        os.environ['TM_E416DEV_SERVER_PASSWORD'],
        os.environ['TM_E416DEV_AGENT']
    )
    assert token_dedi_core.access_token.token

    token_dedi_live = auth.DedicatedServerToken.get(
        auth.AUDIENCE_LIVE,
        os.environ['TM_E416DEV_SERVER_USERNAME'],
        os.environ['TM_E416DEV_SERVER_PASSWORD'],
        os.environ['TM_E416DEV_AGENT']
    )
    assert token_dedi_live.access_token.token

    token_service_core = auth.ServiceToken.get(
        auth.AUDIENCE_CORE,
        os.environ['TM_SERVICE_USERNAME'],
        os.environ['TM_SERVICE_PASSWORD'],
        os.environ['TM_E416DEV_AGENT']
    )
    assert token_service_core.access_token.token

    token_service_live = auth.ServiceToken.get(
        auth.AUDIENCE_LIVE,
        os.environ['TM_SERVICE_USERNAME'],
        os.environ['TM_SERVICE_PASSWORD'],
        os.environ['TM_E416DEV_AGENT']
    )
    assert token_service_live.access_token.token

    token_oauth = auth.OAuthToken.get(
        os.environ['TM_OAUTH_IDENTIFIER'],
        os.environ['TM_OAUTH_SECRET']
    )
    assert token_oauth.access_token.token

    pass


if __name__ == '__main__':
    main()
