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
    if hue < 0 or hue >= 360:
        raise ValueError("Hue value must be in the range [0, 360)")
    
    h = hue / 60
    i = math.floor(h)
    f = h - i
    p = 0
    q = 1 - f
    t = f
    
    if i % 2 == 1:
        q, t = t, q
    
    if i == 0:
        return int(q * 255), int(t * 255), 0
    elif i == 1:
        return int(t * 255), int(q * 255), 0
    elif i == 2:
        return 0, int(q * 255), int(t * 255)
    elif i == 3:
        return 0, int(t * 255), int(q * 255)
    elif i == 4:
        return int(t * 255), 0, int(q * 255)
    else:
        return int(q * 255), 0, int(t * 255)
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