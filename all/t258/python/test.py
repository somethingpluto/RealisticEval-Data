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
        self.assertEqual(bits, '11100010 10000001 10000010')

    def test_empty_byte_array(self):
        byte_array = b""
        char = 'a'
        result = extract_character_bits(byte_array, char)
        self.assertIsNone(result)
