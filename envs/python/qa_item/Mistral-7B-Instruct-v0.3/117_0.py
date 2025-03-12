from typing import Dict
import math

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

    max_val = max(r, g, b)
    min_val = min(r, g, b)
    diff = max_val - min_val

    l = (max_val + min_val) / 2.0

    if max_val == min_val:
        h = s = 0
    elif l > 0.5:
        h = (max_val - b) / diff + (6.0 / 360.0)
    else:
        h = (b - max_val) / diff + (6.0 / 360.0)

    if g <= b:
        s = diff / max_val
    else:
        s = diff / min_val

    result = {"h": h * 360, "s": s * 100, "l": l * 100}
    return result
import unittest


class TestRgbToHsl(unittest.TestCase):

    def test_converts_pure_red_to_hsl(self):
        self.assertEqual(rgb_to_hsl(255, 0, 0), {'h': 0, 's': 100, 'l': 50})

    def test_converts_black_to_hsl(self):
        self.assertEqual(rgb_to_hsl(0, 0, 0), {'h': 0, 's': 0, 'l': 0})

    def test_converts_white_to_hsl(self):
        self.assertEqual(rgb_to_hsl(255, 255, 255), {'h': 0, 's': 0, 'l': 100})

    def test_converts_a_color_on_edge_of_rgb_range(self):
        self.assertEqual(rgb_to_hsl(0, 255, 255), {'h': 180, 's': 100, 'l': 50})

if __name__ == '__main__':
    unittest.main()