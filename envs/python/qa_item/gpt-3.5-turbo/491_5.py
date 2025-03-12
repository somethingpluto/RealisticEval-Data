from typing import Tuple

def convert_range_to_color_yellow_green_change(value: float) -> Tuple[int, int, int]:
    """
    Convert a value in the range [0, 1] to an RGB color that transitions
    from red to yellow and then from yellow to green.

    Parameters:
        value (float): A float value in the range [0, 1] representing the
                       interpolation position.

    Returns:
        tuple: A tuple containing the RGB color values (red, green, blue).
    """

    if value < 0.5:
        red = 255
        green = int(value * 2 * 255)
        blue = 0
    else:
        red = int((1 - value) * 2 * 255)
        green = 255
        blue = 0

    return red, green, blue
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