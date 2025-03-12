def hex_to_ansi(hex_color: str) -> str:
    """
    Convert a hexadecimal color code to an ANSI escape code.

    Args:
        hex_color (str): A string representing the hexadecimal color code, e.g., '#FF5733'.

    Returns:
        str: An ANSI escape code for the specified RGB color.
    """
    if not hex_color.startswith('#') or len(hex_color) != 7:
        raise ValueError("Invalid hexadecimal color code")

    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    return f"\x1b[38;2;{r};{g};{b}m"
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