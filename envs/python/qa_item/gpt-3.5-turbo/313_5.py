from math import sqrt

def is_background_too_dark_or_bright(computed_style):
    def rgb_to_luminance(r, g, b):
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def is_dark(r, g, b):
        luminance = rgb_to_luminance(r, g, b)
        if luminance <= 128:
            return True
        else:
            return False

    def is_bright(r, g, b):
        luminance = rgb_to_luminance(r, g, b)
        if luminance >= 192:
            return True
        else:
            return False

    rgb = computed_style[4:-1].split(',')
    r, g, b = int(rgb[0]), int(rgb[1]), int(rgb[2])

    if is_dark(r, g, b):
        return "dark"
    elif is_bright(r, g, b):
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