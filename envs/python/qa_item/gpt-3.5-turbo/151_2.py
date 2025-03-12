import math

def rgb_to_hsl(rgb: dict) -> dict:
    """
    Converts RGB color values to HSL (Hue, Saturation, Lightness) color values.

    The input RGB values should be in the range of 0 to 255, and the output HSL values will have:
    - `h` (Hue) in the range of 0 to 360,
    - `s` (Saturation) in the range of 0 to 100 (percentage),
    - `l` (Lightness) in the range of 0 to 100 (percentage).

    Args:
        rgb (dict): The RGB color values.
            - rgb['r'] (int): The red color value (0-255).
            - rgb['g'] (int): The green color value (0-255).
            - rgb['b'] (int): The blue color value (0-255).

    Returns:
        dict: A dictionary representing the HSL color values.
            - h (int): The hue value (0-360).
            - s (int): The saturation value (0-100).
            - l (int): The lightness value (0-100).
    """
    r = rgb['r'] / 255
    g = rgb['g'] / 255
    b = rgb['b'] / 255

    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    # Calculate Hue
    if delta == 0:
        h = 0
    elif cmax == r:
        h = (60 * (((g - b) / delta) % 6)) % 360
    elif cmax == g:
        h = (60 * (((b - r) / delta) + 2)) % 360
    else:
        h = (60 * (((r - g) / delta) + 4)) % 360

    # Calculate Lightness
    l = (cmax + cmin) / 2

    # Calculate Saturation
    if delta == 0:
        s = 0
    else:
        s = (delta / (1 - abs(2 * l - 1))) * 100

    return {'h': round(h), 's': round(s), 'l': round(l * 100)}
import unittest


class TestRgbToHsl(unittest.TestCase):

    def test_basic_rgb_red(self):
        rgb = {'r': 255, 'g': 0, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 100, 'l': 50})

    def test_grayscale_middle_gray(self):
        rgb = {'r': 128, 'g': 128, 'b': 128}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 50})

    def test_edge_case_white(self):
        rgb = {'r': 255, 'g': 255, 'b': 255}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 100})

    def test_edge_case_black(self):
        rgb = {'r': 0, 'g': 0, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 0})

    def test_vibrant_green(self):
        rgb = {'r': 0, 'g': 255, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 120, 's': 100, 'l': 50})

    def test_deep_blue(self):
        rgb = {'r': 0, 'g': 0, 'b': 255}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 240, 's': 100, 'l': 50})

if __name__ == '__main__':
    unittest.main()