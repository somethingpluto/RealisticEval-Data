from typing import Dict

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
    
    h /= 360
    s /= 100
    l /= 100
    
    if s == 0:
        r = g = b = l
    else:
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)
    
    return {'r': int(r * 255), 'g': int(g * 255), 'b': int(b * 255)}
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