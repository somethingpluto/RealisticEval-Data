def conv_flags(value: int) -> str:
    # Convert the integer to binary and remove the '0b' prefix
    binary_str = bin(value)[2:]
    # Invert the bits
    inverted_binary_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
    # Convert the inverted binary string to an integer and then to hexadecimal
    inverted_hex_str = hex(int(inverted_binary_str, 2))[2:]
    return inverted_hex_str
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