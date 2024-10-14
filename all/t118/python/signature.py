from typing import Dict


def hsl_to_rgb(h: int, s: int, l: int) -> Dict:
    """
    Converts HSL color values to RGB.

    Args:
        h (int): Hue (0-360 degrees).
        s (int): Saturation (0-100%).
        l (int): Lightness (0-100%).

    Returns:
        Dict: A dictionary containing the RGB values.
    """