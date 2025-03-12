from typing import Tuple
import math

def hue_to_rgb(hue: float) -> Tuple[int, int, int]:
    """
    Converts a hue value to its corresponding RGB color values.

    Args:
        hue (float): A float representing the hue angle in degrees,expected to be in the range [0, 360).

    Returns:
        Tuple[int, int, int]: A tuple containing three integers representing the RGB color components in the range [0, 255]. The first element is the red component, the second element is the green component, and the third element is the blue component.
    """
    if hue < 0 or hue >= 360:
        raise ValueError("Hue value must be in the range [0, 360)")

    c = 255
    X = c * (1 - abs((hue / 60) % 2 - 1))
    m = 0
    r, g, b = 0, 0, 0

    if 0 <= hue < 60:
        r, g, b = c, X, 0
    elif 60 <= hue < 120:
        r, g, b = X, c, 0
    elif 120 <= hue < 180:
        r, g, b = 0, c, X
    elif 180 <= hue < 240:
        r, g, b = 0, X, c
    elif 240 <= hue < 300:
        r, g, b = X, 0, c
    elif 300 <= hue < 360:
        r, g, b = c, 0, X

    r = math.floor((r + m) * 255)
    g = math.floor((g + m) * 255)
    b = math.floor((b + m) * 255)

    return r, g, b
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