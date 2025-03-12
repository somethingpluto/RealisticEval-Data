
from typing import List, Tuple

def calculate_red_proportion(pixels: List[Tuple[int, int, int]]) -> float:
    """
    Analyze a list of pixels, each represented by rgb, and calculate the proportion of red in the list.

    Args:
        pixels (List[Tuple[int, int, int]]): A list of pixels, where each pixel is represented as a tuple of (R, G, B).

    Returns:
        float: The proportion of red in the list of pixels, as a value between 0 and 1.
    """
    # Convert the list of tuples to a list of integers
    pixels_list = list(map(int, pixels.split()))

    # Calculate the sum of red and green values
    red_sum = sum([x[1] for x in pixels_list])
    green_sum = sum([x[0] for x in pixels_list])

    # Calculate the proportion of red in the list
    red_ proportion = red_sum / green_sum

    return red_ proportion

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