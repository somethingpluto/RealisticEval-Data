import base64

def uint8_array_to_base64(uint8_array: bytes) -> str:
    """
    Converts a Uint8Array (or bytes) into a Base64-encoded string.
    The conversion processes the input in groups of 3 bytes,
    resulting in 4 Base64 characters. If the output is less than 3 bytes,
    the result is padded with '=' characters.

    Args:
        uint8_array (bytes): The Uint8Array to be converted (as bytes).

    Returns:
        str: The resulting Base64-encoded string, which may include '=' padding
             if the input length is not a multiple of 3.
    """
    return base64.b64encode(uint8_array).decode('ascii')
import unittest


class TestUint8ArrayToBase64(unittest.TestCase):

    def test_empty_uint8array(self):
        uint8_array = bytes([])  # Empty bytearray
        result = uint8_array_to_base64(uint8_array)
        self.assertEqual(result, '')

    def test_one_byte(self):
        uint8_array = bytes([255])  # One byte
        result = uint8_array_to_base64(uint8_array)
        self.assertEqual(result, '/w==')

    def test_two_bytes(self):
        uint8_array = bytes([255, 255])  # Two bytes
        result = uint8_array_to_base64(uint8_array)
        self.assertEqual(result, '//8=')

    def test_three_bytes(self):
        uint8_array = bytes([255, 255, 255])  # Three bytes
        result = uint8_array_to_base64(uint8_array)
        self.assertEqual(result, '////')

    def test_four_bytes(self):
        uint8_array = bytes([72, 101, 108, 108])  # Four bytes (ASCII for "Hell")
        result = uint8_array_to_base64(uint8_array)
        self.assertEqual(result, 'SGVsbA==')

if __name__ == '__main__':
    unittest.main()