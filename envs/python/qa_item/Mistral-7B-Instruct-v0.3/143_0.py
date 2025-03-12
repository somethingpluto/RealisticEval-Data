def arabic_to_english_numbers(s: str) -> str:
    arabic_to_english = {
        '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
    }
    english_string = ""
    for char in s:
        if char in arabic_to_english:
            english_string += arabic_to_english[char]
        else:
            english_string += char
    return english_string
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