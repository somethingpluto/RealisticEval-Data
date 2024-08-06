from typing import Union


def numerical_str_convert(value: str) -> Union[int, float, str]:
    """
    convert the input string, first see if it is an integer, if it is converted to an integer, if it is not, see if it is a floating point number, if yes, convert to a floating point number, if neither, return the original string

    Args:
        value (str): input str

    Returns:
        Union[int, float, str]: convert result
    """
    try:
        return int(value)
    except ValueError:
        # 如果不是整数，尝试将字符串转换为浮点数
        try:
            return float(value)
        except ValueError:
            # 如果不是整数也不是浮点数，返回原始字符串
            return value
