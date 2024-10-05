from typing import Callable

import inspect


def method_arg_type_check(method_obj: Callable, *args, **kwargs):
    """
    Checks that the arguments passed to a given method object (e.g., method of a class) comply with their
    expected types, based on the method's signature. If there's a discrepancy, it raises a ValueError.

    Args:
        method_obj (Callable): The method for which arguments are checked.
        *args: Positional arguments passed to the method.
        **kwargs: Keyword arguments passed to the method.

    Raises:
        ValueError: If any argument does not match the expected type.
    """
    sig = inspect.signature(method_obj)
    bound_args = sig.bind(*args, **kwargs)

    for param_name, value in bound_args.arguments.items():
        param = sig.parameters[param_name]
        if param.annotation is not param.empty and not isinstance(value, param.annotation):
            raise ValueError(f"Argument '{param_name}' must be of type {param.annotation}, got {type(value).__name__}.")


import unittest
from typing import Callable


class MyClass:
    def my_method(self, arg1: int, arg2: str, optional_arg: float = 3.14):
        pass


class TestMethodArgTypeCheck(unittest.TestCase):
    def test_correct_types(self):
        """ Test with correct argument types. """
        try:
            method_arg_type_check(MyClass.my_method, MyClass(), 10, "hello", optional_arg=3.14)
        except ValueError:
            self.fail("method_arg_type_check() raised ValueError unexpectedly!")




    def test_missing_argument(self):
        """ Test with missing required argument. """
        with self.assertRaises(TypeError):
            method_arg_type_check(MyClass.my_method, MyClass(), 10)  # Missing arg2


if __name__ == '__main__':
    unittest.main()
