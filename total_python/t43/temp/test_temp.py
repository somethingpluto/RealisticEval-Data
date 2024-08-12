import unittest


class TestRGBtoHSV(unittest.TestCase):

    def test_rgb_to_hsv_red(self):
        # Test conversion of pure red color
        r, g, b = 255, 0, 0
        expected_result = (0, 1, 1)  # Hue should be 0, Saturation 1, Value 1 for red
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_green(self):
        # Test conversion of pure green color
        r, g, b = 0, 255, 0
        expected_result = (120, 1, 1)  # Hue should be 120, Saturation 1, Value 1 for green
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_blue(self):
        # Test conversion of pure blue color
        r, g, b = 0, 0, 255
        expected_result = (240, 1, 1)  # Hue should be 240, Saturation 1, Value 1 for blue
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_white(self):
        # Test conversion of white color
        r, g, b = 255, 255, 255
        expected_result = (0, 0, 1)  # Hue is undefined, typically 0; Saturation 0, Value 1 for white
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_black(self):
        # Test conversion of black color
        r, g, b = 0, 0, 0
        expected_result = (0, 0, 0)  # Hue is undefined, typically 0; Saturation 0, Value 0 for black
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)
def rgb_to_hsv(r, g, b):
    # Normalize the RGB values by dividing by 255
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # Find the minimum and maximum values among R, G, and B
    max_rgb = max(r, g, b)
    min_rgb = min(r, g, b)
    delta = max_rgb - min_rgb

    # Calculate H (Hue)
    if delta == 0:
        h = 0
    elif max_rgb == r:
        h = ((g - b) / delta) % 6
    elif max_rgb == g:
        h = ((b - r) / delta) + 2
    else:
        h = ((r - g) / delta) + 4

    h *= 60  # Convert to degrees on the color circle

    # Calculate S (Saturation)
    if max_rgb == 0:
        s = 0
    else:
        s = delta / max_rgb

    # V (Value) is equal to max_rgb
    v = max_rgb

    return (h, s, v)
