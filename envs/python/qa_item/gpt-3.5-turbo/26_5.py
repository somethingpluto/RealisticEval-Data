def convert_to_comma_separated(input_string: str) -> str:
    import re
    
    separators = ['*', ';', '/', '-', ':']
    
    for sep in separators:
        input_string = re.sub(f'[{sep}]', ',', input_string)
    
    return input_string
import unittest


class TestConvertToCommaSeparated(unittest.TestCase):
    def test_basic_separators(self):
        self.assertEqual(convert_to_comma_separated("apple;banana*orange/mango"), "apple,banana,orange,mango",
                         "Failed to convert basic separators.")

    def test_mixed_separators(self):
        self.assertEqual(convert_to_comma_separated("grapes;lemon/melon*kiwi;litchi"), "grapes,lemon,melon,kiwi,litchi",
                         "Failed to convert mixed separators in a string.")
    def test_mixed_separators2(self):
        self.assertEqual(convert_to_comma_separated("grapes/lemon/melon*kiwi*litchi"), "grapes,lemon,melon,kiwi,litchi",
                         "Failed to convert mixed separators in a string.")

    def test_no_separators(self):
        self.assertEqual(convert_to_comma_separated("watermelon"), "watermelon",
                         "Failed when no separators are present.")
if __name__ == '__main__':
    unittest.main()