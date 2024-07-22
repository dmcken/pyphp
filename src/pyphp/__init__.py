'''Index of pyphp module'''
# Read version from installed package
from importlib.metadata import version
__version__ = version("pyphp")

# Bring in top level functions
from .pyphp import http_build_query
