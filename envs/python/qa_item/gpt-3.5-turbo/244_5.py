from typing import Callable

def method_arg_type_check(method_obj: Callable, *args, **kwargs):
    sig = inspect.signature(method_obj)
    params = sig.parameters
    exclude = kwargs.get("exclude", [])
    
    for param_name, param in params.items():
        if param_name in exclude:
            continue
        
        if param.default != inspect.Parameter.empty:
            continue
        
        arg_value = None
        
        if param.kind == param.VAR_POSITIONAL:
            arg_value = args
        elif param.kind == param.VAR_KEYWORD:
            arg_value = kwargs
        elif param_name in kwargs:
            arg_value = kwargs[param_name]
        elif len(args) > 0:
            arg_value = args[0]
            args = args[1:]
        
        if arg_value is not None and not isinstance(arg_value, param.annotation):
            raise ValueError(f"Argument {param_name} is not of type {param.annotation}")

        if len(args) == 0 and param.default == inspect.Parameter.empty and param.kind not in [param.VAR_POSITIONAL, param.VAR_KEYWORD]:
            break
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