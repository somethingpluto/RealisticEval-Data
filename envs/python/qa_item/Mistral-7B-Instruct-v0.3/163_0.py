def binary_string_to_uint8_array(binary_str: str) -> bytearray:
    """
    Stores a second-level string in a set of 8-bit conversion integers in a bytearray and returns.

    Args:
        binary_str (str): The binary string to be converted.

    Returns:
        bytearray: The resulting bytearray containing the binary question.
    """
    return bytearray.fromhex(binary_str.zfill(len(binary_str) // 8 * 2))
import unittest


class TestBinaryStringToUint8Array(unittest.TestCase):

    def test_convert_full_byte_binary_string(self):
        binary_str = '11001010'
        result = binary_string_to_uint8_array(binary_str)
        self.assertEqual(result, bytearray([202]))

    def test_convert_multiple_full_byte_binary_strings(self):
        binary_str = '1100101011110000'
        result = binary_string_to_uint8_array(binary_str)
        self.assertEqual(result, bytearray([202, 240]))

    def test_handle_empty_binary_string(self):
        binary_str = ''
        result = binary_string_to_uint8_array(binary_str)
        self.assertEqual(result, bytearray([]))

    def test_convert_binary_string_with_leading_zeros(self):
        binary_str = '00101101'
        result = binary_string_to_uint8_array(binary_str)
        self.assertEqual(result, bytearray([45]))

    def test_handle_binary_string_with_end_padding_of_zeros(self):
        binary_str = '11001010000'  # should be treated as '11001010 00000000'
        result = binary_string_to_uint8_array(binary_str)
        self.assertEqual(result, bytearray([202, 0]))

if __name__ == '__main__':
    unittest.main()