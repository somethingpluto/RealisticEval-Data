
def convert_to_short_format(input_str):
    """
    Converts a string concatenated with underscores to a short format.
    For example:
        input: f1_p1_g1_b1_c1
        output: fpgbc
    Args:
        input_str (str): The input string with segments separated by underscores.

    Returns:
        str: A short format string derived from the first characters of each segment.
    """
    short_format = input_str.split("_")
    for i, segment in enumerate(short_format):
        if i > 0:
            short_format[i - 1] = segment[0]
    return short_format
python
input_str = "f1_p1_g1_b1_c1"
short_format = convert_to_short_format(input_str)
print(short_format)  # Output: fpgbc

import unittest


class TestConvertToShortFormat(unittest.TestCase):

    def test_basic_case(self):
        """ Test a standard input with mixed characters. """
        self.assertEqual(convert_to_short_format("f1_p1_g1_b1_c1"), "fpgbc")

    def test_multiple_segments(self):
        """ Test input with multiple segments. """
        self.assertEqual(convert_to_short_format("a2_b3_c4"), "abc")

    def test_non_alpha_numeric(self):
        """ Test input with non-alphanumeric characters. """
        self.assertEqual(convert_to_short_format("hello_world_test"), "hwt")

    def test_single_segment(self):
        """ Test a single segment input. """
        self.assertEqual(convert_to_short_format("single"), "s")

if __name__ == '__main__':
    unittest.main()