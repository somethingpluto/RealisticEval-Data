from typing import Dict

def hsl_to_rgb(hue: float, saturation: float, lightness: float) -> Dict[str, int]:
    """
    Converts an HSL color value to RGB.

    Assumes hue is in the range [0, 360], and saturation and lightness are in the range [0, 1].
    Returns r, g, and b values in the range [0, 255].

    Args:
        hue (float): The hue of the color (0-360).
        saturation (float): The saturation of the color (0-1).
        lightness (float): The lightness of the color (0-1).

    Returns:
        dict: A dictionary containing the red, green, and blue channels.
            Example: {'r': 255, 'g': 0, 'b': 0}
    """

    if saturation == 0:
        return {'r': int(lightness * 255), 'g': int(lightness * 255), 'b': int(lightness * 255)}

    hue_60 = hue // 60
    c = lightness * (1 - abs(hue % 60 - 360) / 360)
    x = c * (1 - abs(hue % 2 - 1))
    m = lightness - c

    rgb = {
        'r': int((m + c * (6 - hue_60)) * 255),
        'g': int((m + c * (2 - hue_60)) * 255),
        'b': int((m + c * (4 - hue_60)) * 255)
    }

    for channel in rgb:
        rgb[channel] = min(max(rgb[channel], 0), 255)

    if saturation < 1:
        rgb['r'], rgb['g'], rgb['b'] = map(
            lambda c: int(c * (1 - saturation) + m * 255), rgb.values()
        )

    return rgb
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