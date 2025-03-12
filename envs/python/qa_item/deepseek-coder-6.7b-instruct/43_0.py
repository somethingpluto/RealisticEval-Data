from typing import Tuple

def rgb_to_hsv(r: int, g: int, b: int) -> Tuple[int, int, int]:
    """
    Convert RGB color to HSV color.

    Args:
        r (int): Red value (0-255)
        g (int): Green value (0-255)
        b (int): Blue value (0-255)

    Returns:
        Tuple[int, int, int]: HSV value (H: 0-360, S: 0-100, V: 0-100)
    """
    # Normalize RGB values to the range [0, 1]
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # Find the maximum and minimum values among R, G, B
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    delta = max_val - min_val

    # Calculate Hue (H)
    if delta == 0:
        h = 0
    elif max_val == r:
        h = 60 * (((g - b) / delta) % 6)
    elif max_val == g:
        h = 60 * (((b - r) / delta) + 2)
    else:  # max_val == b
        h = 60 * (((r - g) / delta) + 4)

    # Normalize Hue to the range [0, 360]
    h = int(h % 360)

    # Calculate Saturation (S)
    if max_val == 0:
        s = 0
    else:
        s = int((delta / max_val) * 100)

    # Calculate Value (V)
    v = int(max_val * 100)

    return (h, s, v)
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