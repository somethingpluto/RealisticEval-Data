def camel_case_to_capitalized_with_spaces(input_string: str) -> str:
    converted_string = ""
    for char in input_string:
        if char.isupper() and converted_string:
            converted_string += " "
        converted_string += char
    return converted_string.capitalize()
import unittest


class TestCamelCaseConversion(unittest.TestCase):

    def test_simple_camel_case(self):
        input = "thisIsTest"
        expected_output = "This is test"
        self.assertEqual(camel_case_to_capitalized_with_spaces(input), expected_output)

    def test_single_word_lowercase(self):
        input = "example"
        expected_output = "Example"
        self.assertEqual(camel_case_to_capitalized_with_spaces(input), expected_output)

    def test_multiple_uppercase_letters(self):
        input = "thisIsAnExampleString"
        expected_output = "This is an example string"
        self.assertEqual(camel_case_to_capitalized_with_spaces(input), expected_output)

    def test_single_uppercase_letter(self):
        input = "aSingleUppercaseLetterX"
        expected_output = "A single uppercase letter x"
        self.assertEqual(camel_case_to_capitalized_with_spaces(input), expected_output)

    def test_already_capitalized_string(self):
        input = "AlreadyCapitalized"
        expected_output = "Already capitalized"
        self.assertEqual(camel_case_to_capitalized_with_spaces(input), expected_output)
if __name__ == '__main__':
    unittest.main()