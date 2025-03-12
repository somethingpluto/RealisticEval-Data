from typing import Callable
import inspect

def method_arg_type_check(method_obj: Callable, *args, **kwargs):
    # Get the signature of the method
    signature = inspect.signature(method_obj)

    # Bind the arguments to the signature
    bound_args = signature.bind(*args, **kwargs)

    # Extract the arguments and their default values
    arguments = bound_args.arguments
    defaults = signature.parameters.values()

    # Check the types of the arguments
    for arg, value in arguments.items():
        param = signature.parameters[arg]

        # If the parameter has a default value, skip it
        if param.default is not inspect.Parameter.empty:
            continue

        # If the parameter is annotated with a type, check the type of the argument
        if param.annotation is not inspect.Parameter.empty:
            if not isinstance(value, param.annotation):
                raise ValueError(f"Argument '{arg}' should be of type {param.annotation.__name__}, not {type(value).__name__}")

        # If the parameter is not annotated, check if the argument is a subclass of the default value
        elif defaults:
            default = next((default for default in defaults if default.name == arg), None)
            if default is not None and not isinstance(value, type(default.default)):
                raise ValueError(f"Argument '{arg}' should be a subclass of {type(default.default).__name__}, not {type(value).__name__}")
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