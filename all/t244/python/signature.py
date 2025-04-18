from typing import Callable


import inspect


def method_arg_type_check(method_obj, *args, **kwargs):
    """
    Checks that the arguments passed to a given method object (e.g., method of a class) comply with their
    expected question types, based on the method's signature.js.py.py.py.py.js.js.js. If there's a discrepancy, it raises a ValueError.

    Args:
        method_obj (Callable): The method for which arguments are checked.
        *args (): Positional arguments passed to the method.
        **kwargs (): Keyword arguments passed to the method.


    Optional argument:
        exclude (list of str): Names of parameters to exclude from the type check.

    Returns:

    """
