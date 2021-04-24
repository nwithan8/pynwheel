# A Python client for Pinwheel's API
[![PyPi](https://static.pepy.tech/personalized-badge/pynwheel?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pypi.org/project/pynwheel)
[![License](https://img.shields.io/pypi/l/pynwheel?color=orange&style=flat-square)](https://github.com/nwithan8/pynwheel/blob/master/LICENSE)

[![Open Issues](https://img.shields.io/github/issues-raw/nwithan8/pynwheel?color=gold&style=flat-square)](https://github.com/nwithan8/pynwheel/issues?q=is%3Aopen+is%3Aissue)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/nwithan8/pynwheel?color=black&style=flat-square)](https://github.com/nwithan8/pynwheel/issues?q=is%3Aissue+is%3Aclosed)
[![Latest Release](https://img.shields.io/github/v/release/nwithan8/pynwheel?color=red&label=latest%20release&logo=github&style=flat-square)](https://github.com/nwithan8/pynwheel/releases)

[![Discord](https://img.shields.io/discord/472537215457689601?color=blue&logo=discord&style=flat-square)](https://discord.gg/7jGbCJQ)
[![Twitter](https://img.shields.io/twitter/follow/nwithan8?label=%40nwithan8&logo=twitter&style=flat-square)](https://twitter.com/nwithan8)

Interact with Pinwheel's API in Python

# Installation
From PyPi: ``python -m pip install pynwheel``

From GitHub ``python -m pip install git+https://github.com/nwithan8/pynwheel.git``

# Usage
Can retrieve data from Pinwheel's API as raw JSON or pydantic objects

Import the ``pynwheel`` package to initialize the API
Example:

```python
import pynwheel

api = pynwheel.API(api_type=pynwheel.APIType.PRODUCTION, api_key="thisisanapikey")
```

Set ``raw=True`` to return JSON data, ``raw=False`` to return objects.
NOTE: Object creation not supported yet. Will default to JSON responses.

# Documentation

Documentation available on [ReadTheDocs](https://pynwheel.readthedocs.io/en/latest/documentation.html)