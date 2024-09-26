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
