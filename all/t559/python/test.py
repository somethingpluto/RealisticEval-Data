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
