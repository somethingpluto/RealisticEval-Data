from typing import Callable

def method_arg_type_check(method_obj: Callable, *args, **kwargs):
    """
    Checks that the arguments passed to a given method object (e.g., method of a class) comply with their
    expected question types, based on the method's signature. If there's a discrepancy, it raises a ValueError.

    Args:
        method_obj (Callable): The method for which arguments are checked.
        *args (): Positional arguments passed to the method.
        **kwargs (): Keyword arguments passed to the method.

    Optional argument:
        exclude (list of str): Names of parameters to exclude from the type check.

    Returns:
    """
    sig = inspect.signature(method_obj)
    params = sig.parameters
    arg_dict = {**dict(zip(params, args)), **kwargs}

    for param_name, param_info in params.items():
        if param_name in kwargs.get('exclude', []):
            continue
        if param_info.default != inspect.Parameter.empty and param_name not in arg_dict:
            continue
        if param_name not in arg_dict:
            raise ValueError(f"Missing value for parameter '{param_name}'")
        arg_value = arg_dict[param_name]
        if not isinstance(arg_value, param_info.annotation):
            raise ValueError(f"Argument '{param_name}' should be of type {param_info.annotation.__name__}")

# Usage example:
# def example_function(a: int, b: str): pass
# method_arg_type_check(example_function, 10, b="test")
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