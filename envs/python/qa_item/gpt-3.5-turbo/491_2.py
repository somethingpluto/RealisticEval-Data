import math

def convert_range_to_color_yellow_green_change(value: float) -> tuple:
    def interpolate_color(color1, color2, t):
        return color1 * (1 - t) + color2 * t

    def get_color(value, start_color, middle_color, end_color):
        if value < 0.5:
            t = value / 0.5
            return interpolate_color(start_color, middle_color, t)
        else:
            t = (value - 0.5) / 0.5
            return interpolate_color(middle_color, end_color, t)

    red = get_color(value, 255, 255, 0)
    green = get_color(value, 0, 255, 0)
    blue = 0

    return int(red), int(green), int(blue)
import unittest
class TestConvertToColorThroughYellow(unittest.TestCase):
    
    def test_red(self):
        """Test the output for value 0.0 (should be red)"""
        self.assertEqual(convert_to_color_through_yellow(0.0), (255, 127.5, 127.5))

    def test_yellow(self):
        """Test the output for value 0.5 (should be yellow)"""
        self.assertEqual(convert_to_color_through_yellow(0.5), (255, 255, 127.5))

    def test_green(self):
        """Test the output for value 1.0 (should be green)"""
        self.assertEqual(convert_to_color_through_yellow(1.0), (0, 255, 127.5))

    def test_mid_transition(self):
        """Test the output for value 0.25 (between red and yellow)"""
        self.assertEqual(convert_to_color_through_yellow(0.25), (255, 191, 127.5))

    def test_yellow_transition(self):
        """Test the output for value 0.75 (between yellow and green)"""
        self.assertEqual(convert_to_color_through_yellow(0.75), (127, 255, 127.5))
if __name__ == '__main__':
    unittest.main()