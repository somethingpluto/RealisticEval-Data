from typing import List, Tuple


def calculate_red_proportion(pixels: List[Tuple[int, int, int]]) -> float:
    """
    Calculate the proportion of red in a list of pixels.

    Args:
        pixels (List[Tuple[int, int, int]]): A list of pixels, where each pixel is represented as a tuple of (R, G, B).

    Returns:
        float: The proportion of red in the list of pixels, as a value between 0 and 1.
    """
    if not pixels:
        return 0.0

    total_red = 0
    total_intensity = 0

    for (r, g, b) in pixels:
        total_red += r
        total_intensity += (r + g + b)

    # Avoid division by zero
    if total_intensity == 0:
        return 0.0

    red_proportion = total_red / total_intensity
    return red_proportion
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