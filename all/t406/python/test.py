import unittest


class TestColors(unittest.TestCase):

    def test_red(self):
        """Test red color method"""
        self.assertEqual(Colors.red("Hello"), "\033[31mHello\033[0m")

    def test_green(self):
        """Test green color method"""
        self.assertEqual(Colors.green("Hello"), "\033[32mHello\033[0m")

    def test_blue(self):
        """Test blue color method"""
        self.assertEqual(Colors.blue("Hello"), "\033[34mHello\033[0m")

    def test_yellow(self):
        """Test yellow color method"""
        self.assertEqual(Colors.yellow("Hello"), "\033[33mHello\033[0m")

    def test_magenta(self):
        """Test magenta color method"""
        self.assertEqual(Colors.magenta("Hello"), "\033[35mHello\033[0m")

    def test_cyan(self):
        """Test cyan color method"""
        self.assertEqual(Colors.cyan("Hello"), "\033[36mHello\033[0m")