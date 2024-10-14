import unittest


class TestBoolArrayToBinaryString(unittest.TestCase):

    def test_converts_all_true_values(self):
        bool_array = [True, True, True]
        expected = '111'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_converts_all_false_values(self):
        bool_array = [False, False, False]
        expected = '000'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_converts_mixed_true_and_false_values(self):
        bool_array = [True, False, True, False]
        expected = '1010'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_handles_empty_array(self):
        bool_array = []
        expected = ''
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_handles_single_boolean_value(self):
        bool_array = [True]
        expected = '1'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)
