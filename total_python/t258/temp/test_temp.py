import unittest


class TestExtractCharacterBits(unittest.TestCase):
    def test_character_in_byte_array(self):
        byte_array = b"Hello, world!"
        char = 'w'
        position, bits = extract_character_bits(byte_array, char)
        self.assertEqual(position, 7)
        self.assertEqual(bits, '01110111')

    def test_character_not_in_byte_array(self):
        byte_array = b"Hello, world!"
        char = 'x'
        result = extract_character_bits(byte_array, char)
        self.assertIsNone(result)

    def test_non_utf8_encoding(self):
        byte_array = b"\xff\xfe\xfd\xfc"
        char = '\xff'
        result = extract_character_bits(byte_array, char, charset='latin1')
        self.assertIsNotNone(result)
        position, bits = result
        self.assertEqual(position, 0)
        self.assertEqual(bits, '11111111')

    def test_multibyte_character(self):
        byte_array = "こんにちは".encode('utf-8')
        char = 'に'
        position, bits = extract_character_bits(byte_array, char)
        self.assertEqual(position, 2)

    def test_empty_byte_array(self):
        byte_array = b""
        char = 'a'
        result = extract_character_bits(byte_array, char)
        self.assertIsNone(result)

def extract_character_bits(byte_array, char, charset='utf-8'):
    """
    Extracts the position and bits of a specific character from a byte array.

    :param byte_array: The byte array to search within.
    :param char: The character to find in the byte array.
    :param charset: The character encoding of the byte array.
    :return: A tuple of (position, bits) if the character is found, otherwise None.
    """
    try:
        # Decode byte array to string using the specified character set
        string = byte_array.decode(charset)
    except UnicodeDecodeError:
        print("Failed to decode the byte array.")
        return None

    # Check if the character is in the decoded string
    if char in string:
        position = string.index(char)
        # Find the byte position of the character
        byte_position = len(string[:position].encode(charset))

        # Determine the length of the character in bytes
        char_length = len(char.encode(charset))

        # Extract the bits corresponding to the character
        bits = byte_array[byte_position:byte_position + char_length]

        # Convert bits to a human-readable binary string
        bits_as_string = ' '.join(f'{byte:08b}' for byte in bits)

        return position, bits_as_string
    else:
        print(f"The character '{char}' is not in the byte array.")
        return None
