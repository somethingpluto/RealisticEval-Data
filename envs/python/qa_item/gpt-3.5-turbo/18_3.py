import math

def float_to_rgb(value: float) -> tuple:
    """
    convert a floating point number between 0 and 1 to a color from red to green in the color format RGB
    Args:
        value (float): a float between 0 and 1.

    Returns:
        a tuple representing the RGB color.
    """
    if value < 0 or value > 1:
        raise ValueError("Input value must be between 0 and 1.")
    
    hue = (1 - value) * 120 / 360
    r, g, b = 0, 0, 0
    
    i = math.floor(hue * 6)
    f = hue * 6 - i
    p = value * (1 - value)
    q = value * (1 - f * value)
    t = value * (1 - (1 - f) * value)
    
    if i % 6 == 0:
        r, g, b = value, t, p
    elif i % 6 == 1:
        r, g, b = q, value, p
    elif i % 6 == 2:
        r, g, b = p, value, t
    elif i % 6 == 3:
        r, g, b = p, q, value
    elif i % 6 == 4:
        r, g, b = t, p, value
    elif i % 6 == 5:
        r, g, b = value, p, q
        
    return int(r * 255), int(g * 255), int(b * 255)
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