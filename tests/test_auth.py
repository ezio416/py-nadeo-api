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

    pass


if __name__ == '__main__':
    main()
