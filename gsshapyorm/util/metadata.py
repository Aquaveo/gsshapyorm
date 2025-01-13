"""
********************************************************************************
* Name: metadata
* Author: Alan D. Snow
* Created On: April 24, 2017
* License: BSD-3 Clause
********************************************************************************
"""


def version():
    try:
        from .._version import __version__
        return __version__
    except ImportError:
        return "0.0.0"
