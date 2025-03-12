import math

def rgb_to_hsl(rgb: dict) -> dict:
    r = rgb['r'] / 255
    g = rgb['g'] / 255
    b = rgb['b'] / 255

    max_val = max(r, g, b)
    min_val = min(r, g, b)

    chroma = max_val - min_val
    lightness = (max_val + min_val) / 2

    if chroma == 0:
        hue = 0
    elif lightness < 0.5:
        hue = 60 * ((max_val - b) / chroma)
    else:
        hue = 60 * ((max_val - r) / chroma) + 360

    if hue < 0:
        hue += 360

    saturation = (chroma / lightness) * 100

    return {'h': int(hue),'s': int(saturation), 'l': int(lightness * 100)}
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