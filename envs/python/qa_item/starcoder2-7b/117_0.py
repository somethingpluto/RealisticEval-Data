def rgb_to_hsl(r: int, g: int, b: int) -> Dict:
    r /= 255
    g /= 255
    b /= 255

    max_color = max(r, g, b)
    min_color = min(r, g, b)
    diff = max_color - min_color

    if max_color == min_color:
        h = 0
    elif max_color == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif max_color == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    else:
        h = (60 * ((r - g) / diff) + 240) % 360

    if max_color == 0:
        s = 0
    else:
        s = (diff / max_color) * 100

    l = (max_color + min_color) / 2 * 100

    return {'h': h, 's': s, 'l': l}
import unittest


class TestRgbToHsl(unittest.TestCase):

    def test_converts_pure_red_to_hsl(self):
        self.assertEqual(rgb_to_hsl(255, 0, 0), {'h': 0, 's': 100, 'l': 50})

    def test_converts_black_to_hsl(self):
        self.assertEqual(rgb_to_hsl(0, 0, 0), {'h': 0, 's': 0, 'l': 0})

    def test_converts_white_to_hsl(self):
        self.assertEqual(rgb_to_hsl(255, 255, 255), {'h': 0, 's': 0, 'l': 100})

    def test_converts_a_color_on_edge_of_rgb_range(self):
        self.assertEqual(rgb_to_hsl(0, 255, 255), {'h': 180, 's': 100, 'l': 50})

if __name__ == '__main__':
    unittest.main()