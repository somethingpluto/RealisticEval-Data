import base64

def base64_encode(data: bytearray) -> str:
    """
    Encodes a byte array into a Base64 encoded string.
    Args:
        data (bytearray): A bytearray representing the input data to be encoded.

    Returns:
        str: A string containing the Base64 encoded representation of the input data.
    """
    encoded_data = base64.b64encode(data)
    return encoded_data.decode('utf-8')
import unittest


class Tester(unittest.TestCase):
    """Unit tests for Base64 encoding function."""

    def test_empty_input(self):
        """Empty input should return empty string."""
        input_data = bytearray([])
        self.assertEqual(base64_encode(input_data), "")
    
    def test_encode_hello(self):
        """Encoding 'hello' should return 'aGVsbG8='."""
        input_data = bytearray([ord('h'), ord('e'), ord('l'), ord('l'), ord('o')])
        self.assertEqual(base64_encode(input_data), "aGVsbG8=")
    
    def test_encode_world(self):
        """Encoding 'world' should return 'd29ybGQ='."""
        input_data = bytearray([ord('w'), ord('o'), ord('r'), ord('l'), ord('d')])
        self.assertEqual(base64_encode(input_data), "d29ybGQ=")

    def test_encode_foobar(self):
        """Encoding 'foobar' should return 'Zm9vYmFy'."""
        input_data = bytearray([ord('f'), ord('o'), ord('o'), ord('b'), ord('a'), ord('r')])
        self.assertEqual(base64_encode(input_data), "Zm9vYmFy")

    def test_encode_catch2(self):
        """Encoding 'Catch2' should return 'Q2F0Y2gy'."""
        input_data = bytearray([ord('C'), ord('a'), ord('t'), ord('c'), ord('h'), ord('2')])
        self.assertEqual(base64_encode(input_data), "Q2F0Y2gy")
    
    def test_encode_single_byte(self):
        """Encoding single byte 'A' should return 'QQ=='."""
        input_data = bytearray([ord('A')])
        self.assertEqual(base64_encode(input_data), "QQ==")

if __name__ == '__main__':
    unittest.main()