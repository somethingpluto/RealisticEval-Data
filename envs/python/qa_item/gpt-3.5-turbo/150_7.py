from typing import Dict


def rgb_to_hex(rgb: Dict):
    red = rgb.get('r', 0)
    green = rgb.get('g', 0)
    blue = rgb.get('b', 0)
    
    hex_color = "#{:02X}{:02X}{:02X}".format(red, green, blue)
    
    return hex_color


def hex_to_rgb(hex_color: str):
    if len(hex_color) != 7 or hex_color[0] != '#':
        return None
    
    try:
        red = int(hex_color[1:3], 16)
        green = int(hex_color[3:5], 16)
        blue = int(hex_color[5:], 16)
        
        return {'r': red, 'g': green, 'b': blue}
    except ValueError:
        return None
import unittest

class TestColorConversion(unittest.TestCase):
    def test_rgb_to_hex(self):
        rgb = {'r': 255, 'g': 99, 'b': 71}
        result = rgbToHex(rgb)
        self.assertEqual(result, '#ff6347')  # Expected HEX code for RGB(255, 99, 71)

    def test_hex_to_rgb(self):
        hex_code = '#ff6347'
        result = hexToRgb(hex_code)
        self.assertEqual(result, {'r': 255, 'g': 99, 'b': 71})  # Expected RGB object for HEX #ff6347

    def test_invalid_rgb_components(self):
        rgb = {'r': 300, 'g': -10, 'b': 128}
        result = rgbToHex(rgb)
        self.assertEqual(result, '#00c080')  # Clamped values should be "00", valid value should convert to "80"

    def test_invalid_hex_string(self):
        invalid_hex = '#ggg123'
        result = hexToRgb(invalid_hex)
        self.assertIsNone(result)  # Invalid HEX code should return None

    def test_boundary_values_rgb(self):
        rgb_black = {'r': 0, 'g': 0, 'b': 0}
        result_black = rgbToHex(rgb_black)
        self.assertEqual(result_black, '#000000')  # RGB(0, 0, 0) should convert to #000000
        
        rgb_white = {'r': 255, 'g': 255, 'b': 255}
        result_white = rgbToHex(rgb_white)
        self.assertEqual(result_white, '#ffffff')  # RGB(255, 255, 255) should convert to #ffffff

if __name__ == '__main__':
    unittest.main()