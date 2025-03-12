
def float_to_rgb(value: float) -> tuple:
    """
    convert a floating point number between 0 and 1 to a color from red to green in the color format RGB
    Args:
        value (float): a float between 0 and 1.

    Returns:
        a tuple representing the RGB color.
    """
    # Convert the value to a string in the range [0, 1]
    value_str = str(value)
    # Split the string into a list of values
    values = value_str.split()
    # Initialize the RGB values
    r = float('inf')
    g = float('-inf')
    b = float('-inf')
    # Loop through the values and set the corresponding RGB values
    for i in range(len(values)):
        r = values[i]
        g = values[i + 1]
        b = values[i + 2]
        # Return the RGB tuple
        return (r, g, b)

import unittest


class TestFloatToRGB(unittest.TestCase):

    def test_pure_red(self):
        # Value at the lower boundary (0.0) should return pure red
        result = float_to_rgb(0.0)
        self.assertEqual(result, (255, 0, 0))

    def test_pure_green(self):
        # Value at the upper boundary (1.0) should return pure green
        result = float_to_rgb(1.0)
        self.assertEqual(result, (0, 255, 0))

    def test_midpoint(self):
        # Value at 0.5 should return an equal mix of red and green, resulting in yellow
        result = float_to_rgb(0.5)
        self.assertEqual(result, (127, 127, 0))

    def test_quarter_point(self):
        # Value at 0.25 should return more red than green
        result = float_to_rgb(0.25)
        self.assertEqual(result, (191, 63, 0))

    def test_invalid_value(self):
        # Value outside the range [0, 1] should raise a ValueError
        with self.assertRaises(ValueError):
            float_to_rgb(1.5)
if __name__ == '__main__':
    unittest.main()