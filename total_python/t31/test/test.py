import unittest


class TestCalculateRedProportion(unittest.TestCase):

    def test_all_red_pixels(self):
        # All pixels are fully red
        pixels = [(255, 0, 0), (255, 0, 0), (255, 0, 0)]
        result = calculate_red_proportion(pixels)
        self.assertAlmostEqual(result, 1.0)

    def test_no_red_pixels(self):
        # No red component in any pixel
        pixels = [(0, 255, 0), (0, 0, 255), (0, 255, 255)]
        result = calculate_red_proportion(pixels)
        self.assertAlmostEqual(result, 0.0)

    def test_mixed_red_pixels(self):
        # Mixed colors with some red components
        pixels = [(100, 50, 50), (50, 100, 50), (200, 0, 0)]
        total_red = 100 + 50 + 200
        total_intensity = 100 + 50 + 50 + 50 + 100 + 50 + 200 + 0 + 0
        expected_proportion = total_red / total_intensity
        result = calculate_red_proportion(pixels)
        self.assertAlmostEqual(result, expected_proportion)

    def test_empty_pixel_list(self):
        # Empty list of pixels
        pixels = []
        result = calculate_red_proportion(pixels)
        self.assertAlmostEqual(result, 0.0)

    def test_all_black_pixels(self):
        # All pixels are black
        pixels = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
        result = calculate_red_proportion(pixels)
        self.assertAlmostEqual(result, 0.0)