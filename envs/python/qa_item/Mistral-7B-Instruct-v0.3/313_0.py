import re

def is_background_too_dark_or_bright(computed_style):
    match = re.match(r'rgb\(\d+,\s*\d+,\s*\d+\)', computed_style)
    if not match:
        raise ValueError("Invalid RGB color format")

    r, g, b = map(int, match.groups())

    y = (0.299 * r) + (0.587 * g) + (0.114 * b)
    i = (0.596 * r) - (0.274 * g) - (0.322 * b)
    q = (0.211 * r) - (0.523 * g) + (0.311 * b)

    if y > 255:
        return "bright"
    elif y < 128:
        return "dark"
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