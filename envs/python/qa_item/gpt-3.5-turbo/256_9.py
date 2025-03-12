from typing import List

def bits_to_bytes(bits: List[int]) -> bytearray:
    """
    convert an array of binary bits to an array of bytes. Traversing through each bit, composing these bits into bytes, forming a byte every 8 bits, and then storing these bytes in an array and returning it. If the length of the bit array is not a multiple of 8, the last incomplete byte will be discarded.

    Args:
        bits (List[int]): The input array of bits (each element should be 0 or 1).

    Returns:
        An array of bytes constructed from the bits.
    """
    bytes_array = bytearray()
    byte_str = ''
    
    for bit in bits:
        byte_str += str(bit)
        if len(byte_str) == 8:
            byte = int(byte_str, 2)
            bytes_array.append(byte)
            byte_str = ''
    
    return bytes_array
import unittest


class TestBitsToBytes(unittest.TestCase):

    def test_exact_multiple_of_eight(self):
        """Test bit arrays that are exact multiples of 8 bits."""
        bits = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1]
        expected = bytearray([0b10110010, 0b01001111])  # Corrected to match actual byte values
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_incomplete_byte_discarded(self):
        """Test bit arrays where the last bits do not make up a full byte."""
        bits = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1]  # Last two bits should be discarded
        expected = bytearray([0b10110010])
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_empty_bit_array(self):
        """Test an empty bit array."""
        bits = []
        expected = bytearray()
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_single_full_byte(self):
        """Test bit arrays that exactly make one byte."""
        bits = [1, 1, 1, 1, 1, 1, 1, 1]  # Represents the byte 0xFF
        expected = bytearray([0xFF])
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_no_bits_discarded(self):
        """Test bit arrays with multiple of 8 bits and no extra bits."""
        bits = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1]
        expected = bytearray([0xCC, 0x77])  # Corrected the second byte from 0xB7 to 0x77
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()