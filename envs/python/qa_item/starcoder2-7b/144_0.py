def arabic_to_english_numbers(value: str) -> str:
    arabic_numerals = '٠١٢٣٤٥٦٧٨٩'
    english_numerals = '0123456789'
    translation_table = str.maketrans(arabic_numerals, english_numerals)
    return value.translate(translation_table)
import unittest

class TestArabicToEnglishNumbers(unittest.TestCase):
    
    def test_converts_single_arabic_numerals_to_english(self):
        self.assertEqual(arabic_to_english_numbers('١'), '1')
        self.assertEqual(arabic_to_english_numbers('٥'), '5')
        self.assertEqual(arabic_to_english_numbers('٩'), '9')

    def test_converts_a_string_of_arabic_numerals_to_english(self):
        self.assertEqual(arabic_to_english_numbers('٠١٢٣٤٥٦٧٨٩'), '0123456789')

    def test_handles_strings_with_arabic_and_english_numerals_mixed(self):
        self.assertEqual(arabic_to_english_numbers('٠١23٤5'), '012345')

    def test_leaves_non_numeral_characters_unchanged(self):
        self.assertEqual(arabic_to_english_numbers('Hello World!'), 'Hello World!')
        self.assertEqual(arabic_to_english_numbers('2022-٢٠٢٣'), '2022-2023')

    def test_works_with_full_sentences_that_include_arabic_numerals(self):
        self.assertEqual(arabic_to_english_numbers('The year is ٢٠٢٤!'), 'The year is 2024!')

    def test_handles_empty_strings_correctly(self):
        self.assertEqual(arabic_to_english_numbers(''), '')

    def test_processes_arabic_numerals_in_a_complex_mixed_context(self):
        self.assertEqual(arabic_to_english_numbers('Price: ٥٠٠$ and Date: ٢٠٢٣-١٢-٠١'), 'Price: 500$ and Date: 2023-12-01')

if __name__ == '__main__':
    unittest.main()