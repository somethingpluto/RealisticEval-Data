from math import sqrt

def is_background_too_dark_or_bright(computed_style):
    def get_luminance(rgb):
        r, g, b = rgb
        r = r / 255
        g = g / 255
        b = b / 255

        r = 0.03928 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
        g = 0.03928 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
        b = 0.03928 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4

        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def is_too_dark(luminance):
        return luminance < 0.5

    def is_too_bright(luminance):
        return luminance > 0.9

    rgb_values = [int(value) for value in computed_style[4:-1].split(',')]
    luminance = get_luminance(rgb_values)

    if is_too_dark(luminance):
        return "dark"
    elif is_too_bright(luminance):
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