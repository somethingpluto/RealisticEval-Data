def remove_parts_of_string(*strings):
    """
    Remove the part before the first upper case letter and the first lower case letter from the string.

    Args:
        *strings: Accepts one or more strings as variable arguments
    Returns:
        list: A list of modified strings
    """
    def modify_string(s):
        upper_index = next((i for i, char in enumerate(s) if char.isupper()), None)
        lower_index = next((i for i, char in enumerate(s) if char.islower()), None)
        
        if upper_index is not None and lower_index is not None:
            start_index = min(upper_index, lower_index)
            return s[start_index:]
        elif upper_index is not None:
            return s[upper_index:]
        elif lower_index is not None:
            return s[lower_index:]
        else:
            return s

    return [modify_string(s) for s in strings]
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