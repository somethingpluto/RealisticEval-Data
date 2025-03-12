def remove_parts_of_string(*strings):
    """
    Remove the part before the first upper case letter and the first lower case letter from the string

    For example:
        input: 1234AbCde5678
        output: AbCde5678
    Args:
        *strings: Accepts one or more strings as variable arguments
    Returns:
        A list of modified strings
    """
    def remove_parts(s):
        upper_index = len(s)
        lower_index = len(s)
        for i, char in enumerate(s):
            if char.isupper():
                upper_index = i
                break
        for i, char in enumerate(s):
            if char.islower():
                lower_index = i
                break
        return s[max(upper_index, lower_index):]

    return [remove_parts(s) for s in strings]
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