def arabic_to_english_numbers(s: str) -> str:
    """
    Converts Arabic digits in the string to corresponding English digits.

    Args:
        s (str): The input string containing Arabic digits.

    Returns:
        str: The string with Arabic digits converted to English digits.
    """
    arabic_digits = '٠١٢٣٤٥٦٧٨٩'
    english_digits = '0123456789'
    
    # Create a translation table
    translation_table = str.maketrans(arabic_digits, english_digits)
    
    # Translate the string using the translation table
    return s.translate(translation_table)
import unittest
class TestArabicToEnglishNumbers(unittest.TestCase):
    
    def test_convert_arabic_numerals_to_english_numerals(self):
        input_str = "١٢٣٤٥٦٧٨٩٠"
        expected_output = "1234567890"
        self.assertEqual(arabic_to_english_numbers(input_str), expected_output)

    def test_return_same_string_if_no_arabic_numerals(self):
        input_str = "Hello, World!"
        expected_output = "Hello, World!"
        self.assertEqual(arabic_to_english_numbers(input_str), expected_output)

    def test_handle_mixed_arabic_numerals_and_english_characters(self):
        input_str = "رقم ١٢٣ هو المثال"
        expected_output = "رقم 123 هو المثال"
        self.assertEqual(arabic_to_english_numbers(input_str), expected_output)

    def test_handle_empty_string(self):
        input_str = ""
        expected_output = ""
        self.assertEqual(arabic_to_english_numbers(input_str), expected_output)

    def test_handle_string_with_mixed_arabic_and_english_numerals(self):
        input_str = "The number is ٣٥٦ and 789."
        expected_output = "The number is 356 and 789."
        self.assertEqual(arabic_to_english_numbers(input_str), expected_output)
if __name__ == '__main__':
    unittest.main()