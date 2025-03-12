from typing import Dict
import math

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
    c = (1 - abs(2 * lightness - 1)) * saturation
    x = c * (1 - abs((hue / 60) % 2 - 1))
    m = lightness - c / 2
    
    if hue < 60:
        r, g, b = c, x, 0
    elif hue < 120:
        r, g, b = x, c, 0
    elif hue < 180:
        r, g, b = 0, c, x
    elif hue < 240:
        r, g, b = 0, x, c
    elif hue < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
        
    return {'r': int((r + m) * 255), 'g': int((g + m) * 255), 'b': int((b + m) * 255)}
import unittest

class TestHSLToRGB(unittest.TestCase):
    def test_converts_black(self):
        self.assertEqual(hsl_to_rgb(0, 0, 0), {'r': 0, 'g': 0, 'b': 0})

    def test_converts_white(self):
        self.assertEqual(hsl_to_rgb(0, 0, 1), {'r': 255, 'g': 255, 'b': 255})

    def test_converts_red(self):
        self.assertEqual(hsl_to_rgb(0, 1, 0.5), {'r': 255, 'g': 0, 'b': 0})

    def test_converts_green(self):
        self.assertEqual(hsl_to_rgb(120, 1, 0.5), {'r': 0, 'g': 255, 'b': 0})

    def test_converts_blue(self):
        self.assertEqual(hsl_to_rgb(240, 1, 0.5), {'r': 0, 'g': 0, 'b': 255})

    def test_handles_maximum_hue(self):
        self.assertEqual(hsl_to_rgb(360, 1, 0.5), {'r': 255, 'g': 0, 'b': 0})
if __name__ == '__main__':
    unittest.main()