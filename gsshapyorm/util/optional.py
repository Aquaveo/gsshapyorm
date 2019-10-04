"""
********************************************************************************
* Name: optional.py
* Author: Nathan Swain
* Created On: 2019 October 3
* Copyright: (c) Aquqveo 2019
* License: BSD 2-Clause
********************************************************************************
"""
import importlib


def import_optional(module, func):
    """
    Attempts to import the given dependencies.
    """
    try:
        imported_module = importlib.import_module(module)
    except ImportError:
        raise ModuleNotFoundError(f'Please install optional dependency "{module}" '
                                  f'to use function/method "{func.__name__}()".') from None

    return imported_module


if __name__ == '__main__':

    def example(a, b, c=''):
        os_path = import_optional('os.path', example)
        print(f'Here is a: {a}')
        print(f'Here is b: {b}')
        if c:
            print(f'Here is c: {c}')
        print(os_path.join(c, a, b))

    example('hello', 'world', c='C:')

