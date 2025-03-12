def print_memory_bits(memory_section: bytes):
    """
    Prints the status of each bit (0 or 1) in the given section of memory.

    Args:
        memory_section (bytes): A bytes object representing the section of memory to be read.

    Returns:
        None
    """
    for byte in memory_section:
        # Convert each byte to its binary representation and remove the '0b' prefix
        binary_representation = bin(byte)[2:]
        # Ensure the binary representation is 8 bits long by padding with leading zeros if necessary
        padded_binary_representation = binary_representation.zfill(8)
        # Print the binary representation
        print(padded_binary_representation)
import unittest
from io import StringIO
import sys


class TestPrintMemoryBits(unittest.TestCase):

    def setUp(self):
        # Capture the output during each test
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Restore the normal stdout
        sys.stdout = sys.__stdout__

    def test_single_byte(self):
        memory_section = bytes([0b10101010])
        print_memory_bits(memory_section)
        output = self.held_stdout.getvalue().strip()
        expected_output = "10101010"
        self.assertEqual(output, expected_output)

    def test_multiple_bytes(self):
        memory_section = bytes([0b11001100, 0b11110000])
        print_memory_bits(memory_section)
        output = self.held_stdout.getvalue().strip()
        expected_output = "11001100\n11110000"
        self.assertEqual(output, expected_output)

    def test_all_zeros(self):
        memory_section = bytes([0b00000000])
        print_memory_bits(memory_section)
        output = self.held_stdout.getvalue().strip()
        expected_output = "00000000"
        self.assertEqual(output, expected_output)

    def test_all_ones(self):
        memory_section = bytes([0b11111111])
        print_memory_bits(memory_section)
        output = self.held_stdout.getvalue().strip()
        expected_output = "11111111"
        self.assertEqual(output, expected_output)
if __name__ == '__main__':
    unittest.main()