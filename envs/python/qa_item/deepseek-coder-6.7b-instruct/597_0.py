from typing import Tuple

def hue_to_rgb(hue: float) -> Tuple[int, int, int]:
    """
    Converts a hue value to its corresponding RGB color values.

    Args:
        hue (float): A float representing the hue angle in degrees, expected to be in the range [0, 360).

    Returns:
        Tuple[int, int, int]: A tuple containing three integers representing the RGB color components in the range [0, 255]. The first element is the red component, the second element is the green component, and the third element is the blue component.
    """
    # Ensure the hue value is within the valid range
    hue = hue % 360
    
    # Convert hue to the range [0, 1]
    hue /= 60.0
    
    # Calculate the RGB components
    c = 1.0
    x = c * (1 - abs((hue % 2) - 1))
    
    if 0 <= hue < 1:
        r, g, b = c, x, 0
    elif 1 <= hue < 2:
        r, g, b = x, c, 0
    elif 2 <= hue < 3:
        r, g, b = 0, c, x
    elif 3 <= hue < 4:
        r, g, b = 0, x, c
    elif 4 <= hue < 5:
        r, g, b = x, 0, c
    else:  # 5 <= hue < 6
        r, g, b = c, 0, x
    
    # Scale the RGB values to the range [0, 255]
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    
    return (r, g, b)
import unittest


class Tester(unittest.TestCase):

    def test_hue_0_red(self):
        r, g, b = hue_to_rgb(0)
        self.assertEqual(r, 255)
        self.assertEqual(g, 0)
        self.assertEqual(b, 0)

    def test_hue_120_green(self):
        r, g, b = hue_to_rgb(120)
        self.assertEqual(r, 0)
        self.assertEqual(g, 255)
        self.assertEqual(b, 0)

    def test_hue_240_blue(self):
        r, g, b = hue_to_rgb(240)
        self.assertEqual(r, 0)
        self.assertEqual(g, 0)
        self.assertEqual(b, 255)

    def test_hue_60_yellow(self):
        r, g, b = hue_to_rgb(60)
        self.assertEqual(r, 255)
        self.assertEqual(g, 255)
        self.assertEqual(b, 0)

    def test_hue_180_cyan(self):
        r, g, b = hue_to_rgb(180)
        self.assertEqual(r, 0)
        self.assertEqual(g, 255)
        self.assertEqual(b, 255)

    def test_hue_300_magenta(self):
        r, g, b = hue_to_rgb(300)
        self.assertEqual(r, 255)
        self.assertEqual(g, 0)
        self.assertEqual(b, 255)

if __name__ == '__main__':
    unittest.main()