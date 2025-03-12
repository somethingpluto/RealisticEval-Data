from typing import List

def hex_to_ansi(hex_color: str) -> str:
    """
    Convert a hexadecimal color code to an ANSI escape code.

    Args:
        hex_color (str): A string representing the hexadecimal color code, e.g., '#FF5733'.

    Returns:
        str: An ANSI escape code for the specified RGB color.
    """
    
    def hex_to_rgb(hex_color: str) -> List[int]:
        hex_color = hex_color.lstrip('#')
        return [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    
    def rgb_to_ansi(rgb: List[int]) -> str:
        r, g, b = rgb
        if r == g == b:
            if r < 8:
                return '30'
            if r < 128:
                return '34'
            return '37'
        
        ansi_color = 16 + 36 * int(r / 255 * 5) + 6 * int(g / 255 * 5) + int(b / 255 * 5)
        return str(ansi_color)
    
    rgb = hex_to_rgb(hex_color)
    ansi_code = rgb_to_ansi(rgb)
    
    return f'\033[38;5;{ansi_code}m'
import unittest


class TestHexToAnsi(unittest.TestCase):

    def test_valid_colors(self):
        """Test valid hex color inputs."""
        self.assertEqual(hex_to_ansi("#FF5733"), "\x1b[38;2;255;87;51m")
        self.assertEqual(hex_to_ansi("#00FF00"), "\x1b[38;2;0;255;0m")
        self.assertEqual(hex_to_ansi("#0000FF"), "\x1b[38;2;0;0;255m")

    def test_black_and_white(self):
        """Test edge cases with black and white colors."""
        self.assertEqual(hex_to_ansi("#000000"), "\x1b[38;2;0;0;0m")  # Black
        self.assertEqual(hex_to_ansi("#FFFFFF"), "\x1b[38;2;255;255;255m")  # White

if __name__ == '__main__':
    unittest.main()