from typing import Callable
import inspect

def method_arg_type_check(method_obj: Callable, *args, **kwargs):
    signature = inspect.signature(method_obj)
    parameters = signature.parameters
    param_names = [param for param in parameters]

    exclude = kwargs.get('exclude', [])

    for param_name, arg in zip(param_names, args):
        if param_name not in exclude and parameters[param_name].annotation != inspect.Parameter.empty:
            if not isinstance(arg, parameters[param_name].annotation):
                raise ValueError(f"Argument {param_name} should be of type {parameters[param_name].annotation}")

    for param_name, arg in kwargs.items():
        if param_name not in exclude and parameters[param_name].annotation != inspect.Parameter.empty:
            if not isinstance(arg, parameters[param_name].annotation):
                raise ValueError(f"Argument {param_name} should be of type {parameters[param_name].annotation}")
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