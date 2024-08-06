from typing import Union


def smart_convert(value: str) -> Union[int, float, str]:
    """_summary_

    Args:
        value (str): _description_

    Returns:
        Union[int, float, str]: _description_
    """
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value
