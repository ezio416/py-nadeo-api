# nadeo-api

<!-- [![tests](https://github.com/ezio416/py416/actions/workflows/tests.yml/badge.svg)](https://github.com/ezio416/py-nadeo-api/actions) -->
<!-- [![docs](https://readthedocs.org/projects/py416/badge/?version=latest)](https://nadeo-api.readthedocs.io/en/latest/) -->
[![PyPI](https://badge.fury.io/py/nadeo-api.svg)](https://pypi.org/project/nadeo-api/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A library to assist with accessing Nadeo's web services API and the public Trackmania API (OAuth2).

The web services API has community-driven documentation [here](https://webservices.openplanet.dev/).\
The main section of this API (named "Core") has an up-to-date list of valid endpoints being kept [here](https://github.com/openplanet-nl/core-api-tracking).\
Most of these endpoints are not documented at all, but you may help supplement the documentation [here](https://github.com/openplanet-nl/nadeoapi-docs).

The public Trackmania API has official documentation [here](https://api.trackmania.com/doc).

Installing the package from PyPI:
```
python -m pip install nadeo-api
```

Using the package:
```
import nadeo_api
import nadeo_api.auth
```
