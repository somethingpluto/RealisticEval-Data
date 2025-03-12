class Colors:

    @staticmethod
    def red(text: str) -> str:
        """text in red color"""
        return f"\033[91m{text}\033[0m"

    @staticmethod
    def green(text: str) -> str:
        """text in green color"""
        return f"\033[92m{text}\033[0m"

    @staticmethod
    def blue(text: str) -> str:
        """text in blue color"""
        return f"\033[94m{text}\033[0m"

    @staticmethod
    def yellow(text: str) -> str:
        """text in yellow color"""
        return f"\033[93m{text}\033[0m"

    @staticmethod
    def magenta(text: str) -> str:
        """text in magenta color"""
        return f"\033[95m{text}\033[0m"

    @staticmethod
    def cyan(text: str) -> str:
        """text in cyan color"""
        return f"\033[96m{text}\033[0m"
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