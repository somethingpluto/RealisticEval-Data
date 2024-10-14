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
