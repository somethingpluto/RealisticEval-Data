import codecs

def hex_string_to_byte_array(hex_str: str) -> bytes:
    """Converts a hexadecimal string into a byte array. Hexadecimal strings are often used to represent binary data
    in a readable format, especially in networking, cryptography, and systems programming.

    Args:
        hex_str (str): The hexadecimal string to be converted. This string should only contain hexadecimal characters
                       (0-9, A-F, a-f). If the string has an odd number of characters, a leading zero is added to ensure
                       proper conversion.

    Returns:
        bytes: A byte array representing the binary data encoded in the hex string.
    """
    hex_str = hex_str.zfill((len(hex_str) + 1) // 2 * 2)  # Ensure even length by adding leading zero if necessary
    return codecs.decode(hex_str, 'hex')
import unittest


class TestHexStringToByteArray(unittest.TestCase):
    def test_normal_hex_string(self):
        hex_str = "1a3f"
        expected = bytes([0x1A, 0x3F])
        self.assertEqual(expected, hex_string_to_byte_array(hex_str),
                         "Should correctly convert a normal hex string")

    def test_odd_length_hex_string(self):
        hex_str = "123"
        expected = bytes([0x01, 0x23])
        self.assertEqual(expected, hex_string_to_byte_array(hex_str),
                         "Should handle odd-length hex strings by prepending zero")

    def test_empty_string(self):
        hex_str = ""
        expected = bytes()
        self.assertEqual(expected, hex_string_to_byte_array(hex_str),
                         "Should return an empty array for an empty string")

    def test_hex_string_with_uppercase(self):
        hex_str = "1A3F"
        expected = bytes([0x1A, 0x3F])
        self.assertEqual(expected, hex_string_to_byte_array(hex_str),
                         "Should correctly handle hex strings with uppercase letters")

if __name__ == '__main__':
    unittest.main()