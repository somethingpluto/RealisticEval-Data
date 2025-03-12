import colorama
from colorama import Fore, Back, Style

class Colors:

    @staticmethod
    def red(text: str) -> str:
        return f"{Fore.RED}{text}{Style.RESET_ALL}"

    @staticmethod
    def green(text: str) -> str:
        return f"{Fore.GREEN}{text}{Style.RESET_ALL}"

    @staticmethod
    def blue(text: str) -> str:
        return f"{Fore.BLUE}{text}{Style.RESET_ALL}"

    @staticmethod
    def yellow(text: str) -> str:
        return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"

    @staticmethod
    def magenta(text: str) -> str:
        return f"{Fore.MAGENTA}{text}{Style.RESET_ALL}"

    @staticmethod
    def cyan(text: str) -> str:
        return f"{Fore.CYAN}{text}{Style.RESET_ALL}"
import unittest

class TestColors(unittest.TestCase):

    def test_red(self):
        """Test the red color method"""
        input_text = "Hello"
        expected_output = "\033[91mHello\033[0m"
        self.assertEqual(Colors.red(input_text), expected_output)

    def test_green(self):
        """Test the green color method"""
        input_text = "Hello"
        expected_output = "\033[92mHello\033[0m"
        self.assertEqual(Colors.green(input_text), expected_output)

    def test_blue(self):
        """Test the blue color method"""
        input_text = "Hello"
        expected_output = "\033[94mHello\033[0m"
        self.assertEqual(Colors.blue(input_text), expected_output)

    def test_yellow(self):
        """Test the yellow color method"""
        input_text = "Hello"
        expected_output = "\033[93mHello\033[0m"
        self.assertEqual(Colors.yellow(input_text), expected_output)

    def test_magenta(self):
        """Test the magenta color method"""
        input_text = "Hello"
        expected_output = "\033[95mHello\033[0m"
        self.assertEqual(Colors.magenta(input_text), expected_output)

    def test_cyan(self):
        """Test the cyan color method"""
        input_text = "Hello"
        expected_output = "\033[96mHello\033[0m"
        self.assertEqual(Colors.cyan(input_text), expected_output)

    def test_combined_colors(self):
        """Test combining different color methods"""
        input_text_red = Colors.red("Red")
        input_text_blue = Colors.blue("Blue")
        input_text_combined = f"{input_text_red} and {input_text_blue}"
        expected_output = "\033[91mRed\033[0m and \033[94mBlue\033[0m"
        self.assertEqual(input_text_combined, expected_output)

if __name__ == '__main__':
    unittest.main()