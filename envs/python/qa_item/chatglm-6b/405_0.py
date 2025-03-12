
def remove_parts_of_string(*strings):
    """
    Remove the part before the first upper case letter and the first lower case letter from the string

    For example:
        input: 1234AbCde5678
        output: AbCde5678
    Args:
        *strings: Accepts one or more strings as variable arguments
    Returns:

    """
    # Get the first character of each string
    first_upper_case = strings[0].upper()
    first_lower_case = strings[0].lower()
    
    # Remove the first character of each string
    for string in strings[1:]:
        if first_upper_case in string:
            first_upper_case = string.upper()
        elif first_lower_case in string:
            first_lower_case = string.lower()
        else:
            break
    
    # Remove the first character of each string
    for string in strings[1:]:
        if first_upper_case in string:
            string = string.lower()
        elif first_lower_case in string:
            string = string.upper()
        else:
            break
    
    return string.replace(" ", "")
python
input_string = "1234AbCde5678"
output_string = remove_parts_of_string(input_string)
print(output_string)  # Output: AbCde5678

import unittest


class TestRemovePartsOfString(unittest.TestCase):

    def test_case_3(self):
        # Test with a string that has no uppercase letters
        result = remove_parts_of_string("abcdefg")
        self.assertEqual(result, ["abcdefg"])

    def test_case_4(self):
        # Test with a string that has no lowercase letters
        result = remove_parts_of_string("ABCDEFG")
        self.assertEqual(result, ["ABCDEFG"])

    def test_case_5(self):
        # Test with a string that has mixed cases
        result = remove_parts_of_string("1234AbCde5678")
        self.assertEqual(result, ["AbCde5678"])

    def test_case_6(self):
        # Test with an empty string
        result = remove_parts_of_string("")
        self.assertEqual(result, [""])

    def test_case_7(self):
        # Test with a string that has only one uppercase letter
        result = remove_parts_of_string("X")
        self.assertEqual(result, ["X"])

    def test_case_8(self):
        # Test with a string that has only one lowercase letter
        result = remove_parts_of_string("y")
        self.assertEqual(result, ["y"])

if __name__ == '__main__':
    unittest.main()