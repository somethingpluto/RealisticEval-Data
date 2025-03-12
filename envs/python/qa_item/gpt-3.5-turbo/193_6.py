def conv_flags(value: int) -> str:
    """
    Invert the flag bits of an unsigned integer to a hexadecimal string. The number of bits is not complete by 0.
    Args:
        value (int): The unsigned integer whose bits are to be inverted.

    Returns:
        str: A string containing the hexadecimal representation of the inverted bits.
    """
    hex_value = hex(value ^ (2**value.bit_length() - 1))[2:]
    return hex_value.zfill((len(hex_value) + 3) // 4 * 4)
import unittest

class Tester(unittest.TestCase):
    """
    Test cases for the conv_flags function.
    """
    
    def test_conv_flags(self):
        self.assertEqual(conv_flags(0x0000001F), "FFFFFFE0")
        self.assertEqual(conv_flags(0x00000015), "FFFFFFEA")
        self.assertEqual(conv_flags(0xFFFFFFFF), "0")
        self.assertEqual(conv_flags(0x12345678), "EDCBA987")
        self.assertEqual(conv_flags(0x00000001), "FFFFFFFE")
        self.assertEqual(conv_flags(0x00000003), "FFFFFFFC")
        self.assertEqual(conv_flags(0x00000008), "FFFFFFF7")
        self.assertEqual(conv_flags(0xABCDEF01), "543210FE")

if __name__ == '__main__':
    unittest.main()