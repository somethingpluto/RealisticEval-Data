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
