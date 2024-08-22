import unittest

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

    def test_incorrect_type_for_arg1(self):
        """ Test with incorrect type for arg1. """
        with self.assertRaises(ValueError) as context:
            method_arg_type_check(MyClass.my_method, MyClass(), "10", "hello", optional_arg=3.14)
        self.assertIn("arg1 should be of type int", str(context.exception))

    def test_incorrect_type_for_arg2(self):
        """ Test with incorrect type for arg2. """
        with self.assertRaises(ValueError) as context:
            method_arg_type_check(MyClass.my_method, MyClass(), 10, 10, optional_arg=3.14)
        self.assertIn("arg2 should be of type str", str(context.exception))

    def test_incorrect_type_for_optional_arg(self):
        """ Test with incorrect type for optional_arg. """
        with self.assertRaises(ValueError) as context:
            method_arg_type_check(MyClass.my_method, MyClass(), 10, "hello", optional_arg="pi")
        self.assertIn("optional_arg should be of type float", str(context.exception))

    def test_missing_argument(self):
        """ Test with missing required argument. """
        with self.assertRaises(TypeError):
            method_arg_type_check(MyClass.my_method, MyClass(), 10)  # Missing arg2
import inspect


def method_arg_type_check(method_obj, *args, **kwargs):
    """
    Checks that the arguments passed to a given method object (e.g., method of a class) comply with their
    expected data types, based on the method's signature.js. If there's a discrepancy, it raises a ValueError.

    Parameters:
        method_obj (Callable): The method for which arguments are checked.
        *args: Positional arguments passed to the method.
        **kwargs: Keyword arguments passed to the method.

    Optional argument:
        exclude (list of str): Names of parameters to exclude from the type check.
    """
    # Extract the list of parameters to exclude from the type check from kwargs, defaulting to an empty list if not provided
    exclude = kwargs.pop('exclude', [])
    exclude.append('self')  # Exclude 'self' by default since it refers to the method's instance

    # Get the signature.js of the method and prepare the expected types dictionary
    args_signature = inspect.signature(method_obj)
    bound_args = args_signature.bind(*args, **kwargs)
    bound_args.apply_defaults()

    expected_types = {
        param.name: param.annotation for param in args_signature.parameters.values()
        if param.name not in exclude and param.annotation is not inspect.Parameter.empty
    }

    # Check each argument against its expected type
    for arg_name, arg_type in expected_types.items():
        if arg_name in bound_args.arguments:
            actual_value = bound_args.arguments[arg_name]
            if not isinstance(actual_value, arg_type):
                passed_arg_type = type(actual_value).__name__
                expected_arg_type = arg_type.__name__
                raise ValueError(
                    f"{arg_name} should be of type {expected_arg_type}, but got type {passed_arg_type} instead.")