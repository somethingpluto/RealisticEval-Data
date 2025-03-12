def camel_case_to_capitalized_with_spaces(input_string: str) -> str:
    """
    Converts a camelCase string to a format with the first letter capitalized and spaces between words.

    Args:
        input_string (str): The camelCase string to be converted.

    Returns:
        str: The converted string with spaces and initial capitalization.
    """
    if not input_string:
        return input_string

    result = []
    for i, char in enumerate(input_string):
        if i == 0:
            result.append(char.upper())
        elif char.isupper():
            result.append(' ')
            result.append(char.lower())
        else:
            result.append(char)

    return ''.join(result)
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