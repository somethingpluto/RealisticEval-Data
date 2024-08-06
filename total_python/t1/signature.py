from typing import Union


def numerical_str_convert(value: str) -> Union[int, float, str]:
    """
    convert the input string, first see if it is an integer, if it is converted to an integer, if it is not, see if it is a floating point number, if yes, convert to a floating point number, if neither, return the original string
    Args:
        value (): input value str

    Returns: convert result

    """