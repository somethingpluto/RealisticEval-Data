def rgb_to_hsl(rgb: dict) -> dict:
    r = rgb['r'] / 255
    g = rgb['g'] / 255
    b = rgb['b'] / 255

    max_color = max(r, g, b)
    min_color = min(r, g, b)
    diff = max_color - min_color

    if max_color == min_color:
        h = 0
    elif max_color == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif max_color == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    elif max_color == b:
        h = (60 * ((r - g) / diff) + 240) % 360

    if max_color == 0:
        s = 0
    else:
        s = (diff / max_color) * 100

    l = (max_color + min_color) / 2 * 100

    return {'h': h, 's': s, 'l': l}
import unittest


class TestRgbToHsl(unittest.TestCase):

    def test_basic_rgb_red(self):
        rgb = {'r': 255, 'g': 0, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 100, 'l': 50})

    def test_grayscale_middle_gray(self):
        rgb = {'r': 128, 'g': 128, 'b': 128}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 50})

    def test_edge_case_white(self):
        rgb = {'r': 255, 'g': 255, 'b': 255}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 100})

    def test_edge_case_black(self):
        rgb = {'r': 0, 'g': 0, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 0})

    def test_vibrant_green(self):
        rgb = {'r': 0, 'g': 255, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 120, 's': 100, 'l': 50})

    def test_deep_blue(self):
        rgb = {'r': 0, 'g': 0, 'b': 255}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 240, 's': 100, 'l': 50})

if __name__ == '__main__':
    unittest.main()