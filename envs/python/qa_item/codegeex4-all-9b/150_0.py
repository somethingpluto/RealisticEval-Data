from typing import Dict, Optional

def rgb_to_hex(rgb: Dict) -> str:
    """
    Convert an RGB color object to a HEX color string.

    Args:
        rgb (dict): An object containing the red, green, and blue components of the color.
                    Example: {'r': 255, 'g': 0, 'b': 0}

    Returns:
        str: A string representing the HEX color code.
             Example: "#FF0000" for red.
    """
    return "#{:02X}{:02X}{:02X}".format(rgb['r'], rgb['g'], rgb['b'])

def hex_to_rgb(hex_color: str) -> Optional[Dict]:
    """
    Convert a HEX color string to an RGB color object.

    Args:
        hex_color (str): A string representing the HEX color code.
                         Example: "#FF0000" for red.

    Returns:
        dict or None: An object containing the red, green, and blue components of the color.
                       Returns None if the HEX code is invalid.
                       Example: {'r': 255, 'g': 0, 'b': 0} for red.
    """
    hex_color = hex_color.strip('#')
    if len(hex_color) != 6:
        return None
    try:
        r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        return {'r': r, 'g': g, 'b': b}
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