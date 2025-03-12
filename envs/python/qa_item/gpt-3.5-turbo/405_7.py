from string import ascii_lowercase, ascii_uppercase

def remove_parts_of_string(*strings):
    for string in strings:
        first_upper_index = -1
        first_lower_index = -1
        
        for i, c in enumerate(string):
            if c in ascii_uppercase:
                first_upper_index = i
                break
        
        for i, c in enumerate(string):
            if c in ascii_lowercase:
                first_lower_index = i
                break
        
        if first_upper_index != -1 and first_lower_index != -1:
            return string[first_upper_index:first_lower_index+1]
        else:
            return string
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