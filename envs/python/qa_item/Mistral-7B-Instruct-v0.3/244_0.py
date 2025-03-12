from typing import Callable, TypeVar, Any
import inspect
from typing_extensions import TypedDict

T = TypeVar('T')

class MethodArg(TypedDict):
    name: str
    annotation: type

def method_arg_type_check(method_obj: Callable, *args, **kwargs, exclude: list[str] = []):
    """
    Checks that the arguments passed to a given method object comply with their
    expected question types, based on the method's signature. If there's a discrepancy, it raises a ValueError.

    Args:
        method_obj (Callable): The method for which arguments are checked.
        *args (): Positional arguments passed to the method.
        **kwargs (): Keyword arguments passed to the method.
        exclude (list of str): Names of parameters to exclude from the type check.

    Returns:
        None
    """
    sig = inspect.signature(method_obj)
    for name, param in sig.parameters.items():
        if name in exclude:
            continue
        arg_type = param.annotation
        if arg_type is inspect.Parameter.empty:
            arg_type = Any
        if not isinstance(arg_type, type):
            raise TypeError(f"Unexpected type '{arg_type}' for argument '{name}'")
        if not issubclass(arg_type, object):
            if not isinstance(args[sig.parameters[name].index], arg_type):
                raise ValueError(f"Argument '{name}' has incorrect type. Expected '{arg_type}', got {type(args[sig.parameters[name].index])}")
        elif not isinstance(args[sig.parameters[name].index], arg_type):
            raise ValueError(f"Argument '{name}' has incorrect type. Expected '{arg_type.__name__}', got {type(args[sig.parameters[name].index]).__name__}")

    for name, arg in kwargs.items():
        if name in exclude:
            continue
        if name not in sig.parameters:
            raise ValueError(f"Keyword argument '{name}' not found in method signature")
        arg_type = sig.parameters[name].annotation
        if arg_type is inspect.Parameter.empty:
            arg_type = Any
        if not isinstance(arg_type, type):
            raise TypeError(f"Unexpected type '{arg_type}' for argument '{name}'")
        if not issubclass(arg_type, object):
            if not isinstance(arg, arg_type):
                raise ValueError(f"Keyword argument '{name}' has incorrect type. Expected '{arg_type}', got {type(arg)}")
        elif not isinstance(arg, arg_type):
            raise ValueError(f"Keyword argument '{name}' has incorrect type. Expected '{arg_type.__name__}', got {type(arg).__name__}")
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