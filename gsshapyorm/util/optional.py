"""
********************************************************************************
* Name: optional.py
* Author: Nathan Swain
* Created On: 2019 October 3
* Copyright: (c) Aquqveo 2019
* License: BSD 2-Clause
********************************************************************************
"""
from functools import wraps
import importlib


def optional_dependency(*dependencies):
    """
    Attempts to import the given dependencies.
    """
    def decorator(func):
        for dependency in list(dependencies):
            try:
                importlib.import_module(dependencies)
            except ImportError:
                raise ModuleNotFoundError(f'The "{dependency}" optional dependency is required to run {func}.')
        @wraps(func)
        def _wrap(*args, **kwargs):
            # call the decorated function
            return func(*args, **kwargs)
        return _wrap
    return decorator


if __name__ == '__main__':
    @optional_dependency('foo')
    def example(a, b):
        print(f'Here is a: {a}')
        print(f'Here is b: {b}')
        
    example('hello', 'world')

