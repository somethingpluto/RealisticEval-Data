
def camel_case_to_capitalized_with_spaces(input_string: str) -> str:
    """
    Initialize the camelCase string to a format where only the first letter is capitalized and there are spaces between words.
    Args:
        input_string (str): The camelCase string to be converted.

    Returns:
        str: The converted string with spaces and initial capitalization.
    """
    # Split the input string into words
    words = input_string.split()

    # Initialize an empty list to store the capitalize words
    capitalized_words = []

    # Iterate over the words and capitalize the first letter of each word
    for word in words:
        if len(word) > 0:
            capitalized_words.append(word[0].upper())
        else:
            capitalized_words.append(word)

    # Join the capitalized words with spaces
    capitalized_string = " ".join(capitalized_words)

    return capitalize_string
python
input_string = " camelCase string to be converted"
result = camel_case_to_capitalized_with_spaces(input_string)
print(result)  # Output: camelCase string to be converted

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