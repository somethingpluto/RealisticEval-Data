import math

def float_to_rgb(value: float) -> tuple:
    value = max(0, min(1, value))
    h = (1.0 - value) * 120
    h = math.floor(h)
    s = 1.0
    v = 1.0
    h_i = math.floor(h / 60)
    f = h / 60 - h_i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)

    if h_i == 0:
        return int(v * 255), int(t * 255), int(p * 255)
    elif h_i == 1:
        return int(q * 255), int(v * 255), int(p * 255)
    elif h_i == 2:
        return int(p * 255), int(v * 255), int(t * 255)
    elif h_i == 3:
        return int(p * 255), int(q * 255), int(v * 255)
    elif h_i == 4:
        return int(t * 255), int(p * 255), int(v * 255)
    else:
        return int(v * 255), int(p * 255), int(q * 255)
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