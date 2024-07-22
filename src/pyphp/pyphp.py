'''
PHP helper functions.

'''

# Syetem imports
import collections
import logging
import urllib.parse

# Globals
logger = logging.getLogger(__name__)

# Functions
def http_build_query(data: dict) -> str:
    """PHP's http_build_query

    Initial version taken from:
    https://www.darklaunch.com/http-build-query-in-python-like-php-http-build-query.html

    Args:
        data (dict[str,str]): dictionary to turn into query string.

    Returns:
        str: query_string
    """
    dct = collections.OrderedDict()
    for key, value in data.items():
        if isinstance(value, str):
            dct[key] = value
        elif isinstance(value, list):
            for index, v in enumerate(value):
                dct[f'{key}[{index}]'] = v
        elif isinstance(value, dict):
            for v_key, v_value in value.items():
                dct[f'{key}[{v_key}]'] = v_value
    # Now return the flattened dict
    return urllib.parse.urlencode(dct)
