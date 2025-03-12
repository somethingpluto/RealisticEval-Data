from typing import List

def hex_to_ansi(hex_color: str) -> str:
    hex_color = hex_color.lstrip('#')
    rgb = list(int(hex_color[i:i+2], 16) for i in (0, 2 ,4))
    
    code_list = []
    for color in rgb:
        code = 16 + (color // 256) * 36 + ((color % 256) // 51) * 6 + (color % 256) % 51
        code_list.append(str(code))
    
    return '\x1b[38;5;{}m'.format(';'.join(code_list))
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