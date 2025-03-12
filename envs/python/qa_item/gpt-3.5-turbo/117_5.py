from typing import Dict
from math import floor

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
    
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin
    
    if delta == 0:
        h = 0
    elif cmax == r:
        h = 60 * (((g - b) / delta) % 6)
    elif cmax == g:
        h = 60 * (((b - r) / delta) + 2)
    elif cmax == b:
        h = 60 * (((r - g) / delta) + 4)
        
    l = (cmax + cmin) / 2
    
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))
    
    return {
        'h': round(h),
        's': round(s * 100),
        'l': round(l * 100)
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