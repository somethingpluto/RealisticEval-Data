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
    # Normalize RGB values to be between 0 and 1
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Find the maximum and minimum values
    max_color = max(r, g, b)
    min_color = min(r, g, b)
    diff = max_color - min_color

    # Calculate lightness
    lightness = (max_color + min_color) / 2

    # Calculate saturation
    if max_color == min_color:
        saturation = 0
    else:
        if lightness <= 0.5:
            saturation = diff / (max_color + min_color)
        else:
            saturation = diff / (2 - max_color - min_color)

    # Calculate hue
    if max_color == r:
        hue = (g - b) / diff
    elif max_color == g:
        hue = 2 + (b - r) / diff
    else:
        hue = 4 + (r - g) / diff

    hue *= 60
    if hue < 0:
        hue += 360

    return {"h": hue, "s": saturation, "l": lightness}
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