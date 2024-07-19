from typing import Union


def numerical_str_convert(value: str) -> Union[int, float, str]:
    """
    Intelligently converts the type of the input value. Attempts are made to convert the input value to an integer, if that fails then to a floating-point number, and if both fail, the original value is returned.
    :param value:
    :return:
    """
