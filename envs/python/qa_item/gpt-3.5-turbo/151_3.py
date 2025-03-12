import math

def rgb_to_hsl(rgb: dict) -> dict:
    r = rgb['r'] / 255
    g = rgb['g'] / 255
    b = rgb['b'] / 255

    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    l = (cmax + cmin) / 2

    if delta == 0:
        h = 0
        s = 0
    else:
        if l < 0.5:
            s = delta / (cmax + cmin)
        else:
            s = delta / (2 - cmax - cmin)

        if cmax == r:
            h = 60 * (((g - b) / delta) % 6)
        elif cmax == g:
            h = 60 * (((b - r) / delta) + 2)
        else:
            h = 60 * (((r - g) / delta) + 4)

    return {'h': math.floor(h), 's': math.floor(s * 100), 'l': math.floor(l * 100})
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