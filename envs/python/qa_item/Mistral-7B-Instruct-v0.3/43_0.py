from typing import Tuple

def rgb_to_hsv(r: int, g: int, b: int) -> Tuple[int, int, int]:
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    delta = max_val - min_val

    if max_val == 0:
        h = 0
    elif max_val == min_val:
        h = 0
    elif max_val == r:
        h = (g - b) / delta
    elif max_val == g:
        h = 2 + (b - r) / delta
    elif max_val == b:
        h = 4 + (r - g) / delta

    h *= 60

    if h < 0:
        h += 360

    v = max_val / 255
    s = 0
    if v > 0:
        s = delta / max_val

    return int(h), int(s * 255), int(v * 255)
import unittest


class TestRGBtoHSV(unittest.TestCase):

    def test_rgb_to_hsv_red(self):
        # Test conversion of pure red color
        r, g, b = 255, 0, 0
        expected_result = (0, 100, 100)  # Hue should be 0, Saturation 1, Value 1 for red
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_green(self):
        # Test conversion of pure green color
        r, g, b = 0, 255, 0
        expected_result = (120, 100, 100)  # Hue should be 120, Saturation 1, Value 1 for green
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_blue(self):
        # Test conversion of pure blue color
        r, g, b = 0, 0, 255
        expected_result = (240, 100, 100)  # Hue should be 240, Saturation 1, Value 1 for blue
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_white(self):
        # Test conversion of white color
        r, g, b = 255, 255, 255
        expected_result = (0, 0, 100)  # Hue is undefined, typically 0; Saturation 0, Value 1 for white
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_black(self):
        # Test conversion of black color
        r, g, b = 0, 0, 0
        expected_result = (0, 0, 0)  # Hue is undefined, typically 0; Saturation 0, Value 0 for black
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)
if __name__ == '__main__':
    unittest.main()