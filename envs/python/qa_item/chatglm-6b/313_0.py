
def is_background_too_dark_or_bright(computed_style):
    """Detecting the light or dark state of the background element and returning the corresponding description string.

    Args:
        computed_style (str): The computed background color in 'rgb(r, g, b)' format.

    Returns:
        str: "dark" if the background is too dark, "bright" if it is too bright, or "normal" if it is neither.
    """
    # Convert the computed style to a tuple of red, green, and blue values
    rgb_values = tuple(computed_style.split())

    # Check if the background color is a valid RGB value
    if len(rgb_values)!= 3:
        return "Invalid color format"

    # Calculate the average red, green, and blue values
    avg_red = sum(rgb_values) / len(rgb_values)
    avg_green = sum(rgb_values[1:]) / len(rgb_values)
    avg_blue = sum(rgb_values[:2]) / len(rgb_values)

    # Check if the average red, green, and blue values are within the range of 0-255
    if avg_red < 0 or avg_red > 255:
        return "Dark"
    elif avg_green < 0 or avg_green > 255:
        return "Bright"
    elif avg_blue < 0 or avg_blue > 255:
        return "Normal"
    else:
        return "In between"

import unittest


class TestBackgroundBrightness(unittest.TestCase):
    def test_dark_background(self):
        """Test for a dark background color."""
        background_color = 'rgb(30, 30, 30)'
        result = is_background_too_dark_or_bright(background_color)
        self.assertEqual(result, 'dark')

    def test_bright_background(self):
        """Test for a bright background color."""
        background_color = 'rgb(250, 250, 250)'
        result = is_background_too_dark_or_bright(background_color)
        self.assertEqual(result, 'bright')

    def test_normal_background(self):
        """Test for a background color with normal brightness."""
        background_color = 'rgb(150, 150, 150)'
        result = is_background_too_dark_or_bright(background_color)
        self.assertEqual(result, 'normal')

    def test_high_red_component(self):
        """Test for a bright color with a high red component."""
        background_color = 'rgb(255, 100, 100)'
        result = is_background_too_dark_or_bright(background_color)
        self.assertEqual(result, 'normal')

    def test_low_green_and_blue(self):
        """Test for a dark color with low green and blue components."""
        background_color = 'rgb(10, 10, 100)'
        result = is_background_too_dark_or_bright(background_color)
        self.assertEqual(result, 'dark')

if __name__ == '__main__':
    unittest.main()