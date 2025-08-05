'''
| Author:   Ezio416
| Created:  2024-12-04
| Modified: 2025-08-05

- Tests for nadeo_api.live
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import src.nadeo_api.auth as auth
import src.nadeo_api.live as live


def main() -> None:
    token: auth.Token = auth.get_token(
        'live',
        os.environ['TM_E416DEV_SERVER_USERNAME'],
        os.environ['TM_E416DEV_SERVER_PASSWORD'],
        os.environ['TM_E416DEV_AGENT'],
        True
    )

    # maps = live.get_maps_royal(token, 144)
    # maps = live.get_maps_seasonal(token, 144)
    # maps = live.get_maps_totd(token, 144)
    # maps = live.get_maps_weekly(token, 144)

    # req = live.get_club_campaign(token, 67469, 99524)  # toe3 cps

    pass


if __name__ == '__main__':
    main()
