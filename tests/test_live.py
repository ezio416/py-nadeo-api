'''
- Tests for nadeo_api.live
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import src.nadeo_api.auth as auth
import src.nadeo_api.config as config
import src.nadeo_api.live as live


def get_club_campaign(token: auth.WebServicesToken) -> dict:
    return live.get_club_campaign(token, 67469, 86937)


def get_map_leaderboard(token: auth.WebServicesToken) -> dict:
    return live.get_map_leaderboard(token, 'YjdVxZlrR85ebY_7vr1ihNkElyj')


def get_maps_royal(token: auth.WebServicesToken) -> dict:
    return live.get_maps_royal(token, 99)


def get_maps_seasonal(token: auth.WebServicesToken) -> dict:
    return live.get_maps_seasonal(token, 99)


def get_maps_totd(token: auth.WebServicesToken) -> dict:
    return live.get_maps_totd(token, 99)


def get_maps_weekly_grand(token: auth.WebServicesToken) -> dict:
    return live.get_maps_weekly_grand(token, 99)


def get_maps_weekly_short(token: auth.WebServicesToken) -> dict:
    return live.get_maps_weekly_short(token, 99)


def main() -> None:
    config.debug_logging = True

    token_dedi = auth.DedicatedServerToken.get(
        live.AUDIENCE,
        os.environ['TM_E416DEV_SERVER_USERNAME'],
        os.environ['TM_E416DEV_SERVER_PASSWORD'],
        os.environ['TM_E416DEV_AGENT']
    )
    assert token_dedi.access_token.token

    token_service = auth.ServiceToken.get(
        live.AUDIENCE,
        os.environ['TM_SERVICE_USERNAME'],
        os.environ['TM_SERVICE_PASSWORD'],
        os.environ['TM_E416DEV_AGENT']
    )
    assert token_service.access_token.token

    club_campaign_dedi = get_club_campaign(token_dedi)
    assert club_campaign_dedi
    club_campaign_service = get_club_campaign(token_service)
    assert club_campaign_service
    # assert club_campaign_dedi == club_campaign_service  # relative timestamp is different

    map_leaderboard_dedi = get_map_leaderboard(token_dedi)
    assert map_leaderboard_dedi
    map_leaderboard_service = get_map_leaderboard(token_service)
    assert map_leaderboard_service
    assert map_leaderboard_dedi == map_leaderboard_service

    maps_royal_dedi = get_maps_royal(token_dedi)
    assert maps_royal_dedi
    maps_royal_service = get_maps_royal(token_service)
    assert maps_royal_service
    # assert maps_royal_dedi == maps_royal_service  # relative timestamp is different

    maps_seasonal_dedi = get_maps_seasonal(token_dedi)
    assert maps_seasonal_dedi
    maps_seasonal_service = get_maps_seasonal(token_service)
    assert maps_seasonal_service
    # assert maps_seasonal_dedi == maps_seasonal_service  # relative timestamp is different

    maps_totd_dedi = get_maps_totd(token_dedi)
    assert maps_totd_dedi
    maps_totd_service = get_maps_totd(token_service)
    assert maps_totd_service
    # assert maps_totd_dedi == maps_totd_service  # relative timestamp is different

    maps_weekly_grand_dedi = get_maps_weekly_grand(token_dedi)
    assert maps_weekly_grand_dedi
    maps_weekly_grand_service = get_maps_weekly_grand(token_service)
    assert maps_weekly_grand_service
    # assert maps_weekly_grand_dedi == maps_weekly_grand_service  # relative timestamp is different

    maps_weekly_short_dedi = get_maps_weekly_short(token_dedi)
    assert maps_weekly_short_dedi
    maps_weekly_short_service = get_maps_weekly_short(token_service)
    assert maps_weekly_short_service
    # assert maps_weekly_short_dedi == maps_weekly_short_service  # relative timestamp is different

    pass


if __name__ == '__main__':
    main()
