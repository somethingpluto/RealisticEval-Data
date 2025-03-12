import re

def remove_parts_of_string(*strings):
    for s in strings:
        upper_case_index = -1
        lower_case_index = -1
        for i, char in enumerate(s):
            if char.isupper() and upper_case_index == -1:
                upper_case_index = i
            if char.islower() and lower_case_index == -1:
                lower_case_index = i
            if upper_case_index != -1 and lower_case_index != -1:
                break
        if upper_case_index != -1 and lower_case_index != -1:
            print(s[upper_case_index:])
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