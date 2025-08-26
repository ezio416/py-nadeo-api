'''
| Author:   Ezio416
| Created:  2025-08-26
| Modified: 2025-08-26

- Custom exception types
'''


class AudienceError(ValueError):
    '''
    - a token of the wrong type was passed to a request
    - inherits from `ValueError`
    '''

    pass


class ParameterError(ValueError):
    '''
    - an invalid parameter was passed to a function
    - inherits from `ValueError`
    '''

    pass


class UsageError(ValueError):
    '''
    - an invalid token type was passed to a function
    - inherits from `ValueError`
    '''

    pass
