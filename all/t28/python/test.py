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
        expected_output = "1 0 1 0 1 0 1 0"
        self.assertEqual(output, expected_output)

    def test_multiple_bytes(self):
        memory_section = bytes([0b11001100, 0b11110000])
        print_memory_bits(memory_section)
        output = self.held_stdout.getvalue().strip()
        expected_output = "1 1 0 0 1 1 0 0\n1 1 1 1 0 0 0 0"
        self.assertEqual(output, expected_output)

    def test_all_zeros(self):
        memory_section = bytes([0b00000000])
        print_memory_bits(memory_section)
        output = self.held_stdout.getvalue().strip()
        expected_output = "0 0 0 0 0 0 0 0"
        self.assertEqual(output, expected_output)

    def test_all_ones(self):
        memory_section = bytes([0b11111111])
        print_memory_bits(memory_section)
        output = self.held_stdout.getvalue().strip()
        expected_output = "1 1 1 1 1 1 1 1"
        self.assertEqual(output, expected_output)