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
    # Normalize RGB values to the range [0, 1]
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0

    # Find the maximum and minimum values among r, g, b
    max_val = max(r, g, b)
    min_val = min(r, g, b)

    # Calculate lightness
    l = (max_val + min_val) / 2.0

    # Calculate saturation
    if max_val == min_val:
        s = 0
        h = 0  # Achromatic (gray)
    else:
        if l < 0.5:
            s = (max_val - min_val) / (max_val + min_val)
        else:
            s = (max_val - min_val) / (2.0 - max_val - min_val)

        # Calculate hue
        if max_val == r:
            h = (g - b) / (max_val - min_val)
        elif max_val == g:
            h = 2.0 + (b - r) / (max_val - min_val)
        else:
            h = 4.0 + (r - g) / (max_val - min_val)

        h = h * 60.0  # Convert hue to degrees
        if h < 0:
            h += 360.0

    # Convert saturation and lightness to percentage
    s = s * 100.0
    l = l * 100.0

    return {
        "h": round(h),
        "s": round(s),
        "l": round(l)
    }
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