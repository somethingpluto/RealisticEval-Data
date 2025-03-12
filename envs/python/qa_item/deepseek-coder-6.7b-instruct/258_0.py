from typing import Tuple, List

def extract_character_bits(byte_array: bytes, char: str, charset='utf-8') -> Tuple[int, str]:
    """
    Extracts the position and bits of a specific character from a byte array.

    Args:
        byte_array (bytes): The byte array to search within
        char (str): The character to find in the byte array
        charset (str): The character encoding of the byte array

    Returns:
        A tuple of (position, bits) if the character is found, otherwise None.
    """
    try:
        # Encode the character to bytes using the specified charset
        char_bytes = char.encode(charset)
        
        # Find the position of the character in the byte array
        position = byte_array.find(char_bytes)
        
        if position == -1:
            # Character not found in the byte array
            return None
        
        # Extract the bits of the character
        bits = ''.join(f'{byte:08b}' for byte in char_bytes)
        
        return (position, bits)
    
    except (UnicodeEncodeError, UnicodeDecodeError):
        # Handle encoding/decoding errors
        return None
import unittest

# Assuming extract_character_bits is imported from your module
# from your_module import extract_character_bits

class TestExtractCharacterBits(unittest.TestCase):

    def test_case_1_valid_utf8(self):
        byte_array = b'Hello, World!'
        char = 'W'
        result = extract_character_bits(byte_array, char, 'utf-8')
        expected_result = (7, '01010111')  # 'W' is at position 7 with binary bits
        self.assertEqual(result, expected_result)

    def test_case_2_non_existent_character(self):
        byte_array = b'This is a test.'
        char = 'z'
        result = extract_character_bits(byte_array, char, 'utf-8')
        self.assertIsNone(result)  # Character 'z' is not in the byte array

    def test_case_3_invalid_encoding(self):
        byte_array = b'\xff\xfe'
        char = 'A'
        result = extract_character_bits(byte_array, char, 'ascii')  # Invalid bytes for ASCII
        self.assertIsNone(result)  # Should handle UnicodeDecodeError and return None

    def test_case_4_valid_utf16(self):
        byte_array = 'Hello, World!'.encode('utf-16')
        char = '!'
        result = extract_character_bits(byte_array, char, 'utf-16')
        expected_result = (12, '00100001 00000000')  # '!' at position 12 in UTF-16 encoding
        self.assertEqual(result, expected_result)

    def test_case_5_special_characters_utf8(self):
        byte_array = 'Python 🐍 is fun!'.encode('utf-8')
        char = '🐍'
        result = extract_character_bits(byte_array, char, 'utf-8')
        expected_result = (7, '11110000 10011111 10010000 10001101')  # Unicode character 🐍 in UTF-8
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()