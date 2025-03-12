
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
    # Convert hue to degrees
    h_degrees = h * 180 / 360

    # Convert saturation and lightness to 0-100
    s_min = min(s, 100)
    s_max = max(s, 100)
    l_min = min(l, 100)
    l_max = max(l, 100)

    # Create a dictionary with RGB values
    rgb_dict = Dict()

    # Loop through hue values
    for i in range(h_degrees):
        # Calculate RGB values for current hue
        r, g, b = 0, 0, 0

        # If saturation is less than or equal to 0, set RGB values to 0
        if s_min <= s <= s_max:
            r, g, b = 0, 0, 0
        else:
            r, g, b = s_max - s_min, s_max - l_min, s_min - l_max

        # Update RGB values
        rgb_dict[f"{h_degrees}:{l_min}:{l_max}{r}{g}{b}] = {h: s/l, s: s/l, l: l/l}

    returnrgb_dict

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
        self.assertEqual(hsl_to_rgb(360, 100, 50), {'r': 0, 'g': 0, 'b': 0})  # Should be the same as hue 0

if __name__ == '__main__':
    unittest.main()