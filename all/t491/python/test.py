import unittest


class TestColorConversion(unittest.TestCase):

    def test_red_color(self):
        """ Test for the value that should return pure red. """
        result = convert_to_color_through_yellow(0.0)
        expected = (255, 127, 0)  # Expecting full red
        self.assertEqual(result, expected)

    def test_yellow_color(self):
        """ Test for the value that should return pure yellow. """
        result = convert_to_color_through_yellow(0.5)
        expected = (255, 255, 0)  # Expecting yellow
        self.assertEqual(result, expected)

    def test_green_color(self):
        """ Test for the value that should return pure green. """
        result = convert_to_color_through_yellow(1.0)
        expected = (0, 255, 0)  # Expecting full green
        self.assertEqual(result, expected)

    def test_midpoint_color(self):
        """ Test for a value that should return a color between red and yellow. """
        result = convert_to_color_through_yellow(0.25)
        expected = (255, 191, 0)  # Expecting a color between red and yellow
        self.assertEqual(result, expected)

    def test_above_one(self):
        """ Test for values above the expected range, should still clamp to green. """
        result = convert_to_color_through_yellow(1.5)
        expected = (0, 255, 0)  # Clamping should result in green
        self.assertEqual(result, expected)