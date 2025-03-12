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
    hue = hue / 360
    q = lightness + saturation * (1 if lightness < 0.5 else 0)
    p = 2 * lightness - q
    hk = hue + 1/3
    hj = hue
    hl = hue - 1/3
    
    def hue_to_rgb(h):
        if h < 0:
            h += 1
        if h > 1:
            h -= 1
        if h < 1/6:
            return p + (q - p) * 6 * h
        if h < 1/2:
            return q
        if h < 2/3:
            return p + (q - p) * (2/3 - h) * 6
        return p
    
    r = int(hue_to_rgb(hk) * 255)
    g = int(hue_to_rgb(hj) * 255)
    b = int(hue_to_rgb(hl) * 255)
    
    return {'r': r, 'g': g, 'b': b}
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