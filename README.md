# nadeo-api

<!-- [![tests](https://github.com/ezio416/py416/actions/workflows/tests.yml/badge.svg)](https://github.com/ezio416/py-nadeo-api/actions) -->
[![docs](https://readthedocs.org/projects/nadeo-api/badge/?version=latest)](https://nadeo-api.readthedocs.io/en/latest/)
[![PyPI](https://badge.fury.io/py/nadeo-api.svg)](https://pypi.org/project/nadeo-api/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A library to assist with accessing Nadeo's web services API and the public Trackmania API (OAuth2).

The web services API has community-driven documentation [here](https://webservices.openplanet.dev/).\
The main section of this API (named "Core") has an up-to-date list of valid endpoints being kept [here](https://github.com/openplanet-nl/core-api-tracking).\
Most of these endpoints are not documented at all, but you may help supplement the documentation [here](https://github.com/openplanet-nl/nadeoapi-docs).

The public Trackmania API has official documentation [here](https://api.trackmania.com/doc).\
There is also community-driven documentation [here](https://webservices.openplanet.dev/oauth/reference) which should be a bit more useful.

Installing the package from PyPI:
```
python -m pip install nadeo-api
```

Using the package:
```py
import nadeo_api         # main module - various things
import nadeo_api.auth    # authentication - required for any endpoint
import nadeo_api.config  # configuration options
import nadeo_api.core    # web services Core endpoints
import nadeo_api.live    # web services Live endpoints
import nadeo_api.meet    # web services Meet endpoints
import nadeo_api.oauth   # OAuth2 endpoints (public API)
import nadeo_api.util    # unnecessary - use the main module instead
```

Configuration options in `nadeo_api.config`:
```py
nadeo_api.config.debug_logging = True            # enable debug logging
nadeo_api.config.wait_between_requests_ms = 500  # change self rate limiting
```
