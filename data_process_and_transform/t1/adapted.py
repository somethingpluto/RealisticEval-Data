from typing import Union


def numerical_str_convert(value: str) -> Union[int, float, str]:
    for conversion in (int, float):
        try:
            return conversion(value)
        except ValueError:
            continue
    return value
