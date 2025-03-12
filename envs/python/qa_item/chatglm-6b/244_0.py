
from typing import Callable
import inspect

def method_arg_type_check(method_obj: Callable, *args, **kwargs) -> None:
    """
    Checks that the arguments passed to a given method object (e.g., method of a class) comply with their
    expected question types, based on the method's signature.js.py.py.py.py.py.py.py.py. If there's a discrepancy, it raises a
    ValueError.

    Args:
        method_obj (Callable): The method for which arguments are checked.
        *args (): Positional arguments passed to the method.
        **kwargs (): Keyword arguments passed to the method.


    Optional argument:
        exclude (list of str): Names of parameters to exclude from the type check.

    Returns:

    """
    try:
        method_arg_type_check_result = method_obj(*args, **kwargs)
        if inspect.isfunction(method_obj) and not any(
            type(arg) in exclude for arg in method_arg_type_check_result.args
        ):
            raise ValueError("Method arguments do not comply with expected question types.")
    except ValueError as e:
        print(f"Error: {e}")

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