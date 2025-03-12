
def conv_flags(value: int) -> str:
    """
    Invert the flag bits of an unsigned integer to a hexadecimal string. The number of bits is not complete by 0.
    Args:
        value (int): The unsigned integer whose bits are to be inverted.

    Returns:
        str: A string containing the hexadecimal representation of the inverted bits.
    """
    # Convert the value to a string in hexadecimal format
    hex_value = str(value)
    # Convert the hexadecimal string to a list of integers
    hex_list = list(map(int, hex_value.split()))
    # Iterate over the list of integers and convert each integer to its corresponding bit
    # in the original value
    for i in range(16):
        # If the current bit is set, set its corresponding bit in the inverted value
        if i % 2 == 1:
             inverted_value = value & (1 << i)
            # Convert the inverted value to a string in hexadecimal format
             inverted_hex = str(inverted_value)
            # Add the current bit to the string
             inverted_hex += hex_list[i]
    # Return the resulting string
    return "".join(inverted_hex)

import unittest

class Tester(unittest.TestCase):
    """
    Test cases for the conv_flags function.
    """
    
    def test_conv_flags_case_1(self):
        self.assertEqual(conv_flags(0x0000001F), "FFFFFFE0")

    def test_conv_flags_case_2(self):
        self.assertEqual(conv_flags(0x00000015), "FFFFFFEA")

    def test_conv_flags_case_3(self):
        self.assertEqual(conv_flags(0xFFFFFFFF), "0")

    def test_conv_flags_case_4(self):
        self.assertEqual(conv_flags(0x12345678), "EDCBA987")

    def test_conv_flags_case_5(self):
        self.assertEqual(conv_flags(0x00000001), "FFFFFFFE")

    def test_conv_flags_case_6(self):
        self.assertEqual(conv_flags(0x00000003), "FFFFFFFC")

    def test_conv_flags_case_7(self):
        self.assertEqual(conv_flags(0x00000008), "FFFFFFF7")

    def test_conv_flags_case_8(self):
        self.assertEqual(conv_flags(0xABCDEF01), "543210FE")
if __name__ == '__main__':
    unittest.main()