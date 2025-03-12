def gaussian_weight(intensity_diff: float, sigma_color: float) -> float:
    """
    Calculate the Gaussian weight based on the difference in intensity and a color standard deviation.

    The Gaussian weight is calculated using the formula:
    weight = exp(- (intensity_diff^2) / (2 * sigma_color^2))

    Args:
        intensity_diff (float): The difference in intensity, which is used to compute the weight.
        sigma_color (float): The standard deviation for the color, affecting the spread of the weight.

    Returns:
        float: The Gaussian weight.
    """
    return exp(- (intensity_diff**2) / (2 * sigma_color**2))
import math
import unittest


class Tester(unittest.TestCase):

    def test_zero_intensity_difference(self):
        # When intensity difference is zero, weight should be 1
        intensity_diff = 0.0
        sigma_color = 1.0  # arbitrary sigma value
        self.assertAlmostEqual(gaussian_weight(intensity_diff, sigma_color), 1.0, delta=0.001)

    def test_positive_intensity_difference(self):
        # A positive intensity difference with a reasonable sigma
        intensity_diff = 2.0
        sigma_color = 2.0
        expected_weight = math.exp(-(intensity_diff ** 2) / (2 * sigma_color ** 2))
        self.assertAlmostEqual(gaussian_weight(intensity_diff, sigma_color), expected_weight, delta=0.001)

    def test_negative_intensity_difference(self):
        # A negative intensity difference should yield the same weight as positive
        intensity_diff = -2.0
        sigma_color = 2.0
        expected_weight = math.exp(-(intensity_diff ** 2) / (2 * sigma_color ** 2))
        self.assertAlmostEqual(gaussian_weight(intensity_diff, sigma_color), expected_weight, delta=0.001)

    def test_small_sigma_color(self):
        # Test with a small sigma value
        intensity_diff = 1.0
        sigma_color = 0.1
        expected_weight = math.exp(-(intensity_diff ** 2) / (2 * sigma_color ** 2))
        self.assertAlmostEqual(gaussian_weight(intensity_diff, sigma_color), expected_weight, delta=0.001)

    def test_large_sigma_color(self):
        # Test with a large sigma value
        intensity_diff = 1.0
        sigma_color = 100.0
        expected_weight = math.exp(-(intensity_diff ** 2) / (2 * sigma_color ** 2))
        self.assertAlmostEqual(gaussian_weight(intensity_diff, sigma_color), expected_weight, delta=0.001)

if __name__ == '__main__':
    unittest.main()