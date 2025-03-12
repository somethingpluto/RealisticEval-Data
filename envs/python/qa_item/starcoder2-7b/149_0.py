def hsl_to_rgb(hue: float, saturation: float, lightness: float) -> Dict[str, int]:
    hue /= 360
    if saturation == 0.0:
        return {'r': int(lightness * 255), 'g': int(lightness * 255), 'b': int(lightness * 255)}
    else:
        if lightness < 0.5:
            q = lightness * (1.0 + saturation)
        else:
            q = lightness + saturation - lightness * saturation
        p = 2.0 * lightness - q
        r = hue_to_rgb(p, q, hue + 1/3)
        g = hue_to_rgb(p, q, hue)
        b = hue_to_rgb(p, q, hue - 1/3)
    return {'r': int(r * 255), 'g': int(g * 255), 'b': int(b * 255)}

def hue_to_rgb(p: float, q: float, t: float) -> float:
    if t < 0:
        t += 1
    if t > 1:
        t -= 1
    if t < 1/6:
        return p + (q - p) * 6 * t
    if t < 1/2:
        return q
    if t < 2/3:
        return p + (q - p) * (2/3 - t) * 6
    return p
import unittest

class TestHSLToRGB(unittest.TestCase):
    def test_converts_black(self):
        self.assertEqual(hsl_to_rgb(0, 0, 0), {'r': 0, 'g': 0, 'b': 0})

    def test_converts_white(self):
        self.assertEqual(hsl_to_rgb(0, 0, 1), {'r': 255, 'g': 255, 'b': 255})

    def test_converts_red(self):
        self.assertEqual(hsl_to_rgb(0, 1, 0.5), {'r': 255, 'g': 0, 'b': 0})

    def test_converts_green(self):
        self.assertEqual(hsl_to_rgb(120, 1, 0.5), {'r': 0, 'g': 255, 'b': 0})

    def test_converts_blue(self):
        self.assertEqual(hsl_to_rgb(240, 1, 0.5), {'r': 0, 'g': 0, 'b': 255})

    def test_handles_maximum_hue(self):
        self.assertEqual(hsl_to_rgb(360, 1, 0.5), {'r': 255, 'g': 0, 'b': 0})
if __name__ == '__main__':
    unittest.main()