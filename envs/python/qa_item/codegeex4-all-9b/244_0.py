from typing import Callable, Any, List

import inspect

def method_arg_type_check(method_obj: Callable, *args: Any, **kwargs: Any, exclude: List[str] = None) -> None:
    """
    Checks that the arguments passed to a given method object (e.g., method of a class) comply with their
    expected question types, based on the method's signature. If there's a discrepancy, it raises a ValueError.

    Args:
        method_obj (Callable): The method for which arguments are checked.
        *args (): Positional arguments passed to the method.
        **kwargs (): Keyword arguments passed to the method.
        exclude (list of str): Names of parameters to exclude from the type check.

    Returns:
        None
    """
    if exclude is None:
        exclude = []

    method_signature = inspect.signature(method_obj)
    bound_arguments = method_signature.bind(*args, **kwargs)
    bound_arguments.apply_defaults()

    for name, value in bound_arguments.arguments.items():
        if name in exclude:
            continue

        param = method_signature.parameters[name]
        expected_type = param.annotation

        if expected_type is not inspect._empty and not isinstance(value, expected_type):
            raise ValueError(f"Argument '{name}' must be of type {expected_type}, but got {type(value)}")
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