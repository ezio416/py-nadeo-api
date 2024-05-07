'''
| Author:  Ezio416
| Created: 2024-05-07
| Updated: 2024-05-07

- Tests for nadeo_api.auth
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import src.nadeo_api.auth as auth


if __name__ == '__main__':
    print(auth.get_token())
