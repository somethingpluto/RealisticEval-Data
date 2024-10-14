import unittest


class TestRgbToHsl(unittest.TestCase):

    def test_basic_rgb_red(self):
        rgb = {'r': 255, 'g': 0, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 100, 'l': 50})

    def test_grayscale_middle_gray(self):
        rgb = {'r': 128, 'g': 128, 'b': 128}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 50})

    def test_edge_case_white(self):
        rgb = {'r': 255, 'g': 255, 'b': 255}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 100})

    def test_edge_case_black(self):
        rgb = {'r': 0, 'g': 0, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 0})

    def test_vibrant_green(self):
        rgb = {'r': 0, 'g': 255, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 120, 's': 100, 'l': 50})

    def test_deep_blue(self):
        rgb = {'r': 0, 'g': 0, 'b': 255}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 240, 's': 100, 'l': 50})
