from typing import Callable, List


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
    signature = inspect.signature(method_obj)
    params = list(signature.parameters.values())[1:]  # Exclude the 'self' parameter for methods
    exclude = kwargs.get('exclude', [])
    
    for param, arg in zip(params, args):
        if param.name not in exclude and not isinstance(arg, param.annotation):
            raise ValueError(f"Argument '{param.name}' should be of type {param.annotation.__name__}")
    
    for key, value in kwargs.items():
        param = signature.parameters.get(key)
        if param and key not in exclude and not isinstance(value, param.annotation):
            raise ValueError(f"Argument '{key}' should be of type {param.annotation.__name__}")
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