
def is_cpp_header_file(file_name: str) -> bool:
    """
    Checks whether a file name is a C++ header file.

    Args:
        file_name (str): The name of the file to check.

    Returns:
        bool: Returns True if the file is a C++ header file, False otherwise.
    """
    # Check if the file extension is ".cpp"
    if file_name.endswith(".cpp"):
        # Get the contents of the file
        with open(file_name, "r") as f:
            contents = f.read()
        
        # Check if the contents match a C++ header file
        # (e.g., "iostream" or "vector")
        if "iostream" in contents or "vector" in contents:
            return True
        else:
            return False
    else:
        return False

import unittest


class TestIsCppHeaderFile(unittest.TestCase):

    def test_returns_true_for_h_file(self):
        self.assertTrue(is_cpp_header_file('example.h'))

    def test_returns_true_for_hpp_file(self):
        self.assertTrue(is_cpp_header_file('example.hpp'))

    def test_returns_false_for_non_header_file_extension(self):
        self.assertFalse(is_cpp_header_file('example.txt'))

    def test_returns_false_for_file_without_extension(self):
        self.assertFalse(is_cpp_header_file('example'))

    def test_returns_false_for_c_file(self):
        self.assertFalse(is_cpp_header_file('example.c'))

if __name__ == '__main__':
    unittest.main()