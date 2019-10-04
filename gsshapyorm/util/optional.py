"""
********************************************************************************
* Name: optional.py
* Author: Nathan Swain
* Created On: 2019 October 3
* Copyright: (c) Aquqveo 2019
* License: BSD 2-Clause
********************************************************************************
"""
import functools
import importlib


def optional_dependency(module):
    """
    Attempts to import the given dependencies.
    """
    def decorator(func):
        try:
            importlib.import_module(module)
        except ImportError:
            raise ModuleNotFoundError(f'Please install optional dependency "{module}" to use function '
                                      f'"{func.__name__}()".')

        @functools.wraps(func)
        def _wraps(*args, **kwargs):
            # call the decorated function
            return func(*args, **kwargs)
        return _wraps

    return decorator


if __name__ == '__main__':

    @optional_dependency('foo')
    def example(a, b):
        print(f'Here is a: {a}')
        print(f'Here is b: {b}')
        
    example('hello', 'world')

