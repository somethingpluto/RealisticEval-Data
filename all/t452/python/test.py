import unittest


class TestConvertBitsToBytes(unittest.TestCase):

    def test_empty_input(self):
        """Test conversion of an empty bits array."""
        self.assertEqual(convert_bits_to_bytes([]), [])  # Expecting an empty list

    def test_full_byte(self):
        """Test conversion of a full byte (8 bits)."""
        bits = [1, 0, 1, 0, 1, 1, 0, 0]  # 0b10101100 = 172
        self.assertEqual(convert_bits_to_bytes(bits), [172])

    def test_two_full_bytes(self):
        """Test conversion of two full bytes (16 bits)."""
        bits = [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0]  # 0b10101100 0b00001100
        self.assertEqual(convert_bits_to_bytes(bits), [172, 12])

    def test_remaining_bits(self):
        """Test conversion with remaining bits less than a byte."""
        bits = [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1]  # 0b10101100 0b00000001
        self.assertEqual(convert_bits_to_bytes(bits), [172, 1])

    def test_all_zero_bits(self):
        """Test conversion of all zero bits."""
        bits = [0, 0, 0, 0, 0, 0, 0, 0]  # 0b00000000 = 0
        self.assertEqual(convert_bits_to_bytes(bits), [0])