import re

def is_background_too_dark_or_bright(computed_style):
    def calculate_luminance(r, g, b):
        r = r / 255
        g = g / 255
        b = b / 255
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    rgb_values = re.findall(r'\d+', computed_style)
    r = int(rgb_values[0])
    g = int(rgb_values[1])
    b = int(rgb_values[2])

    luminance = calculate_luminance(r, g, b)

    if luminance < 0.5:
        return "dark"
    elif luminance > 0.8:
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