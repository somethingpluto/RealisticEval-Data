import unittest

class TestHSLToRGB(unittest.TestCase):
    def test_converts_black(self):
        self.assertEqual(hsl_to_rgb(0, 0, 0), {'r': 0, 'g': 0, 'b': 0})

    def test_converts_white(self):
        self.assertEqual(hsl_to_rgb(0, 0, 1), {'r': 255, 'g': 255, 'b': 255})

    def test_converts_red(self):
        self.assertEqual(hsl_to_rgb(0, 1, 0.5), {'r': 255, 'g': 0, 'b': 0})

    def test_converts_green(self):
        self.assertEqual(hsl_to_rgb(120, 1, 0.5), {'r': 0, 'g': 255, 'b': 0})

    def test_converts_blue(self):
        self.assertEqual(hsl_to_rgb(240, 1, 0.5), {'r': 0, 'g': 0, 'b': 255})

    def test_handles_maximum_hue(self):
        self.assertEqual(hsl_to_rgb(360, 1, 0.5), {'r': 255, 'g': 0, 'b': 0})