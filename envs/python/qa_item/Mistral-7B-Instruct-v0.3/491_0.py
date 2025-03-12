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

    # Scale the input value from the range [0, 1] to [0, 255]
    scaled_value = int(255 * value)

    # Define the RGB values for red, yellow, and green
    red = 255
    yellow_start = 255
    yellow_end = 0
    green = 0

    # Calculate the RGB values based on the scaled value
    if scaled_value <= 127.5:
        red = int(255 * (1 - (scaled_value / 127.5)))
        green = int(255 * (scaled_value / 127.5))
    else:
        red = 0
        green = int(255 * ((scaled_value - 127.5) / 127.5))

    # Adjust the yellow_start and yellow_end values for a smoother transition
    yellow_start = int(255 * (1 - (127.5 / 127.5)))
    yellow_end = int(255 * (127.5 / 127.5))

    # Calculate the actual RGB values for the transition
    if scaled_value <= 63.75:
        rgb = (red, yellow_start + (green - yellow_start) * (scaled_value / 63.75), 0)
    elif scaled_value <= 127.5:
        rgb = (red, yellow_start + ((yellow_end - yellow_start) * ((scaled_value - 63.75) / 63.75)),
               green - ((yellow_end - yellow_start) * ((scaled_value - 63.75) / 63.75)))
    else:
        rgb = (0, yellow_end, green)

    return rgb
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