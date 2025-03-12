from math import floor

def convert_range_to_color_yellow_green_change(value: float) -> tuple:
    def interpolate_color(color1, color2, factor):
        r = color1[0] + factor * (color2[0] - color1[0])
        g = color1[1] + factor * (color2[1] - color1[1])
        b = color1[2] + factor * (color2[2] - color1[2])
        return (int(r), int(g), int(b))

    if value < 0.5:
        red = (255, 0, 0)
        yellow = (255, 255, 0)
        return interpolate_color(red, yellow, value * 2)
    else:
        yellow = (255, 255, 0)
        green = (0, 255, 0)
        return interpolate_color(yellow, green, (value - 0.5) * 2)
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