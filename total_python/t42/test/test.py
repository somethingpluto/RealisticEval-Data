import unittest


class TestReplacePhoneNumbers(unittest.TestCase):

    def test_replace_single_phone_number(self):
        # Test replacement of a single phone number
        text = "My number is +1 234-567-8901."
        expected_result = "My number is [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(text), expected_result)

    def test_replace_multiple_phone_numbers(self):
        # Test replacement of multiple phone numbers in one string
        text = "Call +1 234-567-8901 or +1 (123) 456-7890."
        expected_result = "Call [PHONE_NUM] or [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(text), expected_result)

    def test_replace_international_formats(self):
        # Test replacement of international phone number formats
        text = "UK office: +44 20 7946 0958, US office: (123) 456-7890."
        expected_result = "UK office: [PHONE_NUM], US office: [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(text), expected_result)

    def test_no_phone_numbers_present(self):
        # Test text with no phone numbers
        text = "Please email us for more information."
        expected_result = "Please email us for more information."
        self.assertEqual(replace_phone_numbers(text), expected_result)

    def test_phone_number_with_dots_and_spaces(self):
        # Test replacement of phone numbers using dots and spaces
        text = "Reach me at 123.456.7890 or 123 456 7890."
        expected_result = "Reach me at [PHONE_NUM] or [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(text), expected_result)