import binascii

def hex_string_to_byte_array(hex_str: str) -> bytes:
    hex_str = hex_str.zfill(len(hex_str) + len(hex_str) % 2)  # Add leading zero if needed
    return bytes.fromhex(hex_str)
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