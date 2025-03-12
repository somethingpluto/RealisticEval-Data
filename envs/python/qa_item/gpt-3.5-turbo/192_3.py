def hex_string_to_unsigned_int(hex_string: str) -> int:
    """
    Convert a hexadecimal string representing an unsigned integer to its corresponding unsigned integer value.

    Args:
        hex_string (str): The hexadecimal string to be converted.

    Returns:
        int: The unsigned integer value represented by the hexadecimal string.
    """
    return int(hex_string, 16)
import unittest

class Tester(unittest.TestCase):
    def test_hex_string_to_unsigned_int(self):
        # Valid hex strings
        self.assertEqual(hex_string_to_unsigned_int("1A3F"), 6719)      # 1A3F in hex is 6719 in decimal
        self.assertEqual(hex_string_to_unsigned_int("FFFF"), 65535)     # FFFF in hex is 65535 in decimal
        self.assertEqual(hex_string_to_unsigned_int("0"), 0)            # 0 in hex is 0 in decimal
        self.assertEqual(hex_string_to_unsigned_int("7F"), 127)         # 7F in hex is 127 in decimal
        self.assertEqual(hex_string_to_unsigned_int("ABC123"), 11256099) # ABC123 in hex is 11256099 in decimal

        # Lowercase hex string
        self.assertEqual(hex_string_to_unsigned_int("abcd"), 43981)     # abcd in hex is 43981 in decimal

        # Hex string with leading zeroes
        self.assertEqual(hex_string_to_unsigned_int("0001"), 1)         # 0001 in hex is 1 in decimal

        # Empty hex string
        self.assertEqual(hex_string_to_unsigned_int(""), 0)             # Empty string should be treated as 0

        # Mixed case hex string
        self.assertEqual(hex_string_to_unsigned_int("AbCdEf"), 11259375) # AbCdEf in hex is 11259375 in decimal

if __name__ == '__main__':
    unittest.main()