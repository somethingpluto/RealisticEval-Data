def convert_range_to_color_yellow_green_change(value: float) -> tuple:
    """
    Convert a value in the range [0, 1] to an RGB color that transitions
    from red to yellow and then from yellow to green.

    Parameters:
        value (float): A float value in the range [0, 1] representing the
                       interpolation position.

    Returns:
        tuple: A tuple containing the RGB color values (red, green, blue).
    """
    if not 0 <= value <= 1:
        raise ValueError("Input value must be in the range [0, 1]")

    if value <= 0.5:
        # Transition from red to yellow
        red = 255
        green = int(255 * (2 * value))
        blue = 0
    else:
        # Transition from yellow to green
        red = int(255 * (2 - 2 * value))
        green = 255
        blue = 0

    return (red, green, blue)
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