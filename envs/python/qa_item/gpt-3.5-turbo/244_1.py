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
    signature = inspect.signature(method_obj)
    parameters = signature.parameters

    exclude = kwargs.get('exclude', [])
    args_dict = dict(zip(parameters.keys(), args))

    for key, value in kwargs.items():
        args_dict[key] = value

    for param_name, param in parameters.items():
        if param_name not in exclude and param_name not in args_dict:
            raise ValueError(f"Missing argument: {param_name}")

        if param_name in args_dict:
            if not isinstance(args_dict[param_name], param.annotation):
                raise ValueError(f"Argument {param_name} type mismatch. Expected {param.annotation}, got {type(args_dict[param_name])}")

    return None
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