from typing import Tuple


def rgb_to_hsv(r, g, b) -> Tuple[int, int, int]:
    """
    convert RGB color to HSV color.
    For example:
        input: 0, 0, 255
        output: 240, 100, 100
    Args:
        r (int): rgb read value
        g (int): rgb green value
        b (int): rgb blue value

    Returns:
       Tuple[int, int, int]: HSV value
    """
