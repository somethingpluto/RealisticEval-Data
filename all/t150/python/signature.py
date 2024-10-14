from typing import Dict


def rgb_to_hex(rgb: Dict):
    """
    Convert an RGB color object to a HEX color string.

    Args:
        rgb (dict): An object containing the red, green, and blue components of the color.
                    Example: {'r': 255, 'g': 0, 'b': 0}

    Returns:
        str: A string representing the HEX color code.
             Example: "#FF0000" for red.
    """


def hex_to_rgb(hex_color: str):
    """
    Convert a HEX color string to an RGB color object.

    Args:
        hex_color (str): A string representing the HEX color code.
                         Example: "#FF0000" for red.

    Returns:
        dict or None: An object containing the red, green, and blue components of the color.
                       Returns None if the HEX code is invalid.
                       Example: {'r': 255, 'g': 0, 'b': 0} for red.
    """
