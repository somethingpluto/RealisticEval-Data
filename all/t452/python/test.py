import unittest


class TestConvertBitsToBytes(unittest.TestCase):
    def test_empty_input(self):
        """Test with an empty bit array."""
        self.assertEqual(convert_bits_to_bytes([]), [])

    def test_complete_byte(self):
        """Test with exactly one complete byte (8 bits)."""
        bits = [1, 0, 1, 0, 1, 1, 0, 1]  # Should produce byte 0b10101101 = 173
        self.assertEqual(convert_bits_to_bytes(bits), [173])

    def test_two_complete_bytes(self):
        """Test with two complete bytes (16 bits)."""
        bits = [1, 0, 1, 0, 1, 1, 0, 1,  # First byte: 0b10101101
                0, 1, 1, 0, 1, 0, 0, 1]  # Second byte: 0b01101001
        self.assertEqual(convert_bits_to_bytes(bits), [173, 105])

    def test_incomplete_byte(self):
        """Test with bits that do not complete a byte."""
        bits = [1, 0, 1, 0, 1, 1, 0]  # 7 bits, should produce one byte and an incomplete byte
        self.assertEqual(convert_bits_to_bytes(bits), [173])  # 0b10101101 = 173, remaining 0b0000000

    def test_mixed_bits(self):
        """Test with a mixed array of bits (not forming complete bytes)."""
        bits = [1, 1, 0, 0, 1, 1, 1, 0,  # First byte: 0b11001110 = 206
                0, 0, 1]  # Incomplete byte: 0b00000001 = 1
        self.assertEqual(convert_bits_to_bytes(bits), [206, 1])
