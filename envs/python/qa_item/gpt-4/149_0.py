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
    def hue_to_rgb(p, q, t):
        if t < 0:
            t += 1
        if t > 1:
            t -= 1
        if t < 1/6:
            return p + (q - p) * 6 * t
        if t < 1/2:
            return q
        if t < 2/3:
            return p + (q - p) * (2/3 - t) * 6
        return p

    if saturation == 0:
        r = g = b = int(lightness * 255)
    else:
        q = lightness * (1 + saturation) if lightness < 0.5 else lightness + saturation - lightness * saturation
        p = 2 * lightness - q
        hk = hue / 360
        tr = hk + 1/3
        tg = hk
        tb = hk - 1/3
        r = int(hue_to_rgb(p, q, tr) * 255)
        g = int(hue_to_rgb(p, q, tg) * 255)
        b = int(hue_to_rgb(p, q, tb) * 255)

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