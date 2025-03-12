from typing import Tuple

def hue_to_rgb(hue: float) -> Tuple[int, int, int]:
    """
    Converts a hue value to its corresponding RGB color values.

    Args:
        hue (float): A float representing the hue angle in degrees,expected to be in the range [0, 360).

    Returns:
        Tuple[int, int, int]: A tuple containing three integers representing the RGB color components in the range [0, 255]. The first element is the red component, the second element is the green component, and the third element is the blue component.
    """
    if not 0 <= hue < 360:
        raise ValueError("Hue must be in the range [0, 360).")

    # Normalize hue to [0, 1)
    hue = hue / 360

    # Calculate the RGB components
    if 0 <= hue < 1/3:
        r = 1.0
        g = 3*hue
        b = 0.0
    elif 1/3 <= hue < 2/3:
        r = 1 - 3*(hue - 1/3)
        g = 1.0
        b = 0.0
    else:
        r = 0.0
        g = 1.0
        b = 3*(hue - 2/3)

    # Scale the RGB components to [0, 255]
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