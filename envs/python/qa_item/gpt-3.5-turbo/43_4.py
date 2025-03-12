from typing import Tuple
from math import sqrt

def rgb_to_hsv(r: int, g: int, b: int) -> Tuple[int, int, int]:
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    
    if max_value == min_value:
        h = 0
    elif max_value == r:
        h = 60 * ((g - b) / (max_value - min_value))
    elif max_value == g:
        h = 60 * ((b - r) / (max_value - min_value)) + 120
    else:
        h = 60 * ((r - g) / (max_value - min_value)) + 240
        
    if h < 0:
        h += 360
        
    s = 0 if max_value == 0 else (max_value - min_value) / max_value
    v = max_value
    
    return round(h), round((s * 100)), round((v / 255) * 100)
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