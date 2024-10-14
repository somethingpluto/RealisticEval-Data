from typing import Dict


def hsl_to_rgb(hue: float, saturation: float, lightness: float) -> Dict[str, int]:
    """
    Converts an HSL color value to RGB.

    Assumes hue is in the range [0, 360], and saturation and lightness are in the range [0, 1].
    Returns r, g, and b values in the range [0, 255].

    Args:
        hue (float): The hue of the color (0-360).
        saturation (float): The saturation of the color (0-1).
        lightness (float): The lightness of the color (0-1).

    Returns:
        dict: A dictionary containing the red, green, and blue channels.
            Example: {'r': 255, 'g': 0, 'b': 0}
    """
