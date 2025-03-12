from typing import Dict
import math

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

    h = h % 360
    s = s / 100
    l = l / 100

    if s == 0:
        return {"r": l, "g": l, "b": l}

    chroma = s * (1 - math.abs(l - 0.5))
    x = chroma * (1 if l < 0.5 else 2 - chroma)
    y = chroma * (1 - x)

    r = l + x - (h // 60) * y
    g = l + y - (h // 60) * x
    b = l + (h + 30) // 60 * x - y

    return {"r": max(0, min(r, 1)), "g": max(0, min(g, 1)), "b": max(0, min(b, 1))}
import unittest


class TestHSLToRGB(unittest.TestCase):

    def test_converts_pure_red_hue_correctly(self):
        self.assertEqual(hsl_to_rgb(0, 100, 50), {'r': 255, 'g': 0, 'b': 0})

    def test_returns_gray_for_zero_saturation(self):
        self.assertEqual(hsl_to_rgb(240, 0, 50), {'r': 128, 'g': 128, 'b': 128})

    def test_returns_white_for_full_lightness(self):
        self.assertEqual(hsl_to_rgb(120, 50, 100), {'r': 255, 'g': 255, 'b': 255})

    def test_converts_full_saturation_and_mid_lightness_blue_correctly(self):
        self.assertEqual(hsl_to_rgb(240, 100, 50), {'r': 0, 'g': 0, 'b': 255})

    def test_handles_edge_hue_at_360_degrees_correctly(self):
        self.assertEqual(hsl_to_rgb(360, 100, 50), {'r': 255, 'g': 0, 'b': 0})  # Should be the same as hue 0

if __name__ == '__main__':
    unittest.main()