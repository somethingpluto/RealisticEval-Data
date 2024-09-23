import unittest

class TestColors(unittest.TestCase):

    def test_red(self):
        # Test that the red method returns a string formatted with red color
        self.assertEqual(Colors.red("hello"), '\033[31mhello\033[0m')

    def test_green(self):
        # Test that the green method returns a string formatted with green color
        self.assertEqual(Colors.green("hello"), '\033[32mhello\033[0m')

    def test_blue(self):
        # Test that the blue method returns a string formatted with blue color
        self.assertEqual(Colors.blue("hello"), '\033[34mhello\033[0m')

    def test_yellow(self):
        # Test that the yellow method returns a string formatted with yellow color
        self.assertEqual(Colors.yellow("hello"), '\033[33mhello\033[0m')

    def test_magenta(self):
        # Test that the magenta method returns a string formatted with magenta color
        self.assertEqual(Colors.magenta("hello"), '\033[35mhello\033[0m')

    def test_cyan(self):
        # Test that the cyan method returns a string formatted with cyan color
        self.assertEqual(Colors.cyan("hello"), '\033[36mhello\033[0m')
