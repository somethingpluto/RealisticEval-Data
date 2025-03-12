from typing import List, Tuple

def calculate_red_proportion(pixels: List[Tuple[int, int, int]]) -> float:
    total_pixels = len(pixels)
    total_red = sum([pixel[0] for pixel in pixels])

    if total_pixels == 0:
        return 0.0

    return total_red / total_pixels
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

if __name__ == '__main__':
    unittest.main()