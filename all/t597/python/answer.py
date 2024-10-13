import math
from typing import Tuple

def hue_to_rgb(hue: float) -> Tuple[int, int, int]:
    """
    Ensure the hue value is within the range [0, 360).
    """
    hue = hue % 360.0  # Ensure hue is within [0, 360)
    if hue < 0:
        hue += 360.0

    # Calculate RGB values based on hue
    sector = int(hue / 60)  # Determine the sector
    fractional = (hue / 60) - sector  # Calculate the fractional part

    # Initialize RGB values
    if sector == 0:
        r, g, b = 1.0, fractional, 0.0  # Red to Yellow
    elif sector == 1:
        r, g, b = 1.0 - fractional, 1.0, 0.0  # Yellow to Green
    elif sector == 2:
        r, g, b = 0.0, 1.0, fractional  # Green to Cyan
    elif sector == 3:
        r, g, b = 0.0, 1.0 - fractional, 1.0  # Cyan to Blue
    elif sector == 4:
        r, g, b = fractional, 0.0, 1.0  # Blue to Magenta
    else:
        r, g, b = 1.0, 0.0, 1.0 - fractional  # Magenta to Red

    # Convert to 0-255 range
    red = int(r * 255)
    green = int(g * 255)
    blue = int(b * 255)

    return red, green, blue  # Return RGB as a tuple