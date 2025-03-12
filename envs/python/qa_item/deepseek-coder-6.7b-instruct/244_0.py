from typing import Callable, List, Any
import inspect

def method_arg_type_check(method_obj: Callable, *args: Any, **kwargs: Any) -> None:
    """
    Checks that the arguments passed to a given method object comply with their
    expected types, based on the method's signature. If there's a discrepancy, it raises a ValueError.

    Args:
        method_obj (Callable): The method for which arguments are checked.
        *args (): Positional arguments passed to the method.
        **kwargs (): Keyword arguments passed to the method.

    Optional argument:
        exclude (list of str): Names of parameters to exclude from the type check.

    Raises:
        ValueError: If there is a type mismatch between the provided arguments and the method's signature.
    """
    # Get the signature of the method
    sig = inspect.signature(method_obj)
    bound_args = sig.bind(*args, **kwargs)
    bound_args.apply_defaults()

    # Extract the exclude list from kwargs if provided
    exclude = kwargs.pop('exclude', [])

    # Iterate over the parameters in the signature
    for param_name, param in sig.parameters.items():
        if param_name in exclude:
            continue

        # Get the provided argument value
        provided_value = bound_args.arguments.get(param_name)

        # Get the expected type from the parameter annotation
        expected_type = param.annotation

        # If the parameter is not annotated, skip the check
        if expected_type == inspect.Parameter.empty:
            continue

        # Check if the provided value is of the expected type
        if not isinstance(provided_value, expected_type):
            raise ValueError(f"Argument '{param_name}' must be of type {expected_type}, but got {type(provided_value)}")
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