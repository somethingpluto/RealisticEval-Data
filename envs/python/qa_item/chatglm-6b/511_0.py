
def hex_to_ansi(hex_color: str) -> str:
    """
    Convert a hexadecimal color code to an ANSI escape code.

    Args:
        hex_color (str): A string representing the hexadecimal color code, e.g., '#FF5733'.

    Returns:
        str: An ANSI escape code for the specified RGB color.
    """
    # Convert the hexadecimal color code to a RGB value
    rgb_value = '#'.join([f'{hex_color[:2]}' if i % 2 == 0 else f'{hex_color[i:]}' for i in range(3)])
    # Convert the RGB value to an ANSI escape code
    ANSI_ESCAPE_CODE = f'\x1B[31m' if rgb_value == '000000' else f'\x1B[34m' if rgb_value == '008080' else f'\x1B[35m'

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