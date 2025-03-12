from typing import Tuple
import math

def hue_to_rgb(hue: float) -> Tuple[int, int, int]:
    """
    Converts a hue value to its corresponding RGB color values.

    Args:
        hue (float): A float representing the hue angle in degrees, expected to be in the range [0, 360).

    Returns:
        Tuple[int, int, int]: A tuple containing three integers representing the RGB color components in the range [0, 255]. The first element is the red component, the second element is the green component, and the third element is the blue component.
    """
    if hue < 0 or hue > 360:
        raise ValueError("Hue value should be in the range [0, 360)")

    h = hue / 60
    c = int(255 * (1 - math.fabs(math.fmod(h, 2) - 1)))
    x = int(255 * (h // 6 - math.floor(h // 6)))
    m = int(255 * (1 - c))

    r = 0
    g = 0
    b = 0

    if h >= 0 and h < 60:
        r = c
        g = x
    elif h >= 60 and h < 120:
        g = c
        b = x
    elif h >= 120 and h < 180:
        g = 255
        b = x
    elif h >= 180 and h < 240:
        r = 255 - x
        b = c
    elif h >= 240 and h < 300:
        r = x
        b = c
    elif h >= 300 and h <= 360:
        r = x
        g = c

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