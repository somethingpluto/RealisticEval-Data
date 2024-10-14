from typing import Dict


def rgb_to_hsl(r: int, g: int, b: int) -> Dict:
    """
    Converts an RGB color value to HSL.

    Args:
        r (int): The red component (0-255).
        g (int): The green component (0-255).
        b (int): The blue component (0-255).

    Returns:
        Dict: A dictionary containing the HSL values.
    """
