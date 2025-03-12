def is_background_too_dark_or_bright(computed_style):
    """
    Detecting the light or dark state of the background element and returning the corresponding description string.

    Args:
        computed_style (str): The computed background color in 'rgb(r, g, b)' format.

    Returns:
        str: "dark" if the background is too dark, "bright" if it is too bright, or "normal" if it is neither.
    """
    import re

    def calculate_luminance(r, g, b):
        # Convert RGB to luminance
        r = r / 255
        g = g / 255
        b = b / 255
        if r <= 0.03928:
            r = r / 12.92
        else:
            r = ((r + 0.055) / 1.055) ** 2.4
        if g <= 0.03928:
            g = g / 12.92
        else:
            g = ((g + 0.055) / 1.055) ** 2.4
        if b <= 0.03928:
            b = b / 12.92
        else:
            b = ((b + 0.055) / 1.055) ** 2.4
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    # Extract RGB values from the computed style
    match = re.match(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', computed_style)
    if not match:
        raise ValueError("Invalid RGB format")

    r, g, b = map(int, match.groups())

    # Calculate luminance
    luminance = calculate_luminance(r, g, b)

    # Define thresholds for dark and bright
    dark_threshold = 0.179
    bright_threshold = 0.81

    if luminance <= dark_threshold:
        return "dark"
    elif luminance >= bright_threshold:
        return "bright"
    else:
        return "normal"
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