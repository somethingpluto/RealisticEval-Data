from typing import Tuple

def hue_to_rgb(hue: float) -> Tuple[int, int, int]:
    hue = hue % 360
    if hue < 60:
        r, g, b = 255, int((hue / 60) * 255), 0
    elif hue < 120:
        r, g, b = int(((120 - hue) / 60) * 255), 255, 0
    elif hue < 180:
        r, g, b = 0, 255, int(((hue - 120) / 60) * 255)
    elif hue < 240:
        r, g, b = 0, int(((240 - hue) / 60) * 255), 255
    elif hue < 300:
        r, g, b = int(((hue - 240) / 60) * 255), 0, 255
    else:
        r, g, b = 255, 0, int(((360 - hue) / 60) * 255)
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