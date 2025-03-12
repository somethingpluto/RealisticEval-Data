from typing import Tuple

def rgb_to_hsv(r: int, g: int, b: int) -> Tuple[int, int, int]:
    """
    convert RGB color to HSV color.
    For example:
        input: 0, 0, 255
        output: 240, 100, 100
    Args:
        r (int): rgb red value
        g (int): rgb green value
        b (int): rgb blue value

    Returns:
       Tuple[int, int, int]: HSV value
    """
    
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin
    
    if delta == 0:
        hue = 0
    elif cmax == r:
        hue = int(60 * (((g - b) / delta) % 6))
    elif cmax == g:
        hue = int(60 * (((b - r) / delta) + 2))
    elif cmax == b:
        hue = int(60 * (((r - g) / delta) + 4))
    
    if cmax == 0:
        saturation = 0
    else:
        saturation = int((delta / cmax) * 100)
        
    value = int(cmax * 100)
    
    return hue, saturation, value
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