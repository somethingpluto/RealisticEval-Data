from math import sqrt

def is_background_too_dark_or_bright(computed_style):
    """Detecting the light or dark state of the background element and returning the corresponding description string.

    Args:
        computed_style (str): The computed background color in 'rgb(r, g, b)' format.

    Returns:
        str: "dark" if the background is too dark, "bright" if it is too bright, or "normal" if it is neither.
    """
    def rgb_to_brightness(rgb):
        r, g, b = rgb
        return sqrt(0.299 * r**2 + 0.587 * g**2 + 0.114 * b**2)

    def is_dark(rgb):
        return rgb_to_brightness(rgb) < 130

    def is_bright(rgb):
        return rgb_to_brightness(rgb) > 200

    rgb_values = [int(x) for x in computed_style[4:-1].split(',')]
    if is_dark(rgb_values):
        return "dark"
    elif is_bright(rgb_values):
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