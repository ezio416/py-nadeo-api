'''
- Tests for nadeo_api.meet
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import src.nadeo_api.auth as auth
import src.nadeo_api.config as config
import src.nadeo_api.meet as meet


def get_current_cotd(token: auth.WebServicesToken) -> dict:
    return meet.get_current_cotd(token)


def get_matchmaking_divisions(token: auth.WebServicesToken) -> dict:
    return meet.get_matchmaking_divisions(token, 'ranked-2v2')


def get_matchmaking_ids(token: auth.WebServicesToken) -> dict:
    return meet.get_matchmaking_ids(token)


def get_matchmaking_player_status(token: auth.ServiceToken) -> dict:
    return meet.get_matchmaking_player_status(token, 'ranked-2v2')


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

    current_cotd_dedi = get_current_cotd(token_dedi)
    assert current_cotd_dedi
    current_cotd_service = get_current_cotd(token_service)
    assert current_cotd_service
    assert current_cotd_dedi == current_cotd_service

    matchmaking_divisions_dedi = get_matchmaking_divisions(token_dedi)
    assert matchmaking_divisions_dedi
    matchmaking_divisions_service = get_matchmaking_divisions(token_service)
    assert matchmaking_divisions_service
    assert matchmaking_divisions_dedi == matchmaking_divisions_service

    matchmaking_ids_dedi = get_matchmaking_ids(token_dedi)
    assert matchmaking_ids_dedi
    matchmaking_ids_service = get_matchmaking_ids(token_service)
    assert matchmaking_ids_service
    assert matchmaking_ids_dedi == matchmaking_ids_service

    matchmaking_player_status = get_matchmaking_player_status(token_service)
    assert matchmaking_player_status

    pass


if __name__ == '__main__':
    main()
