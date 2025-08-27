'''
| Author:   Ezio416
| Created:  2025-08-26
| Modified: 2025-08-27

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
    - may also be used if an endpoint is only useful with a Ubisoft account, but a dedicated server account was used
    - inherits from `ValueError`
    '''

    pass
