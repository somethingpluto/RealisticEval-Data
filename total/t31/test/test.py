import unittest

from total.t31.adapted import calculate_anger_level


class TestAngerLevelCalculation(unittest.TestCase):

    def test_all_equal_colors(self):
        pixels = [(100, 100, 100)] * 5
        self.assertEqual(calculate_anger_level(pixels), 120)

    def test_all_angry(self):
        pixels = [(255, 100, 100)] * 10
        self.assertEqual(calculate_anger_level(pixels), 180)

    def test_all_calm(self):
        pixels = [(100, 200, 200)] * 10
        self.assertEqual(calculate_anger_level(pixels), 60)

    def test_mixed_emotions(self):
        pixels = [(255, 0, 0), (0, 255, 255), (128, 128, 128)]
        self.assertEqual(calculate_anger_level(pixels), 120)

