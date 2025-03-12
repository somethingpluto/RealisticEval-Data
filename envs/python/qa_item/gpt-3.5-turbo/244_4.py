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

    for i, arg in enumerate(args):
        param_name = list(params.keys())[i]
        if param_name not in kwargs.get('exclude', []):
            param_type = params[param_name].annotation
            if not isinstance(arg, param_type):
                raise ValueError(f"Argument '{param_name}' should be of type {param_type.__name__}, but got {type(arg).__name__}")

    for k, v in kwargs.items():
        if k != 'exclude':
            if k not in params:
                raise ValueError(f"Unexpected keyword argument: {k}")
            if not isinstance(v, params[k].annotation):
                raise ValueError(f"Argument '{k}' should be of type {params[k].annotation.__name__}, but got {type(v).__name__}")
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