nadeo-api
=========

A library to assist with accessing Nadeo's web services API and the public Trackmania API (OAuth2).

The web services API has community-driven documentation at https://webservices.openplanet.dev/ .

The main section of this API (named "Core") has an up-to-date list of valid endpoints being kept at https://github.com/openplanet-nl/core-api-tracking .

Most of these endpoints are not documented at all, but you may help supplement the documentation at https://github.com/openplanet-nl/nadeoapi-docs .


The public Trackmania API has official documentation at https://api.trackmania.com/doc.

There is also community-driven documentation at https://webservices.openplanet.dev/oauth/reference which should be a bit more useful.

Installing the package from PyPI:
```
python -m pip install nadeo-api
```

Using the package:
```py
import nadeo_api
import nadeo_api.auth   # authentication - required for any endpoint
import nadeo_api.core   # web services Core endpoints
import nadeo_api.live   # web services Live endpoints
import nadeo_api.meet   # web services Meet endpoints
import nadeo_api.oauth  # OAuth2 endpoints (public API)
```


.. include:: modules.rst
