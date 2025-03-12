import math

def rgb_to_hsl(rgb: dict) -> dict:
    r = rgb['r'] / 255
    g = rgb['g'] / 255
    b = rgb['b'] / 255

    max_color = max(r, g, b)
    min_color = min(r, g, b)

    delta = max_color - min_color

    l = (max_color + min_color) / 2

    if delta == 0:
        h = s = 0
    else:
        if l < 0.5:
            s = delta / (max_color + min_color)
        else:
            s = delta / (2 - max_color - min_color)

        if max_color == r:
            h = (g - b) / delta + (6 if g < b else 0)
        elif max_color == g:
            h = (b - r) / delta + 2
        else:
            h = (r - g) / delta + 4

        h *= 60
        h = round(h)
        s = round(s * 100)
        l = round(l * 100)

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