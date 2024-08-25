import unittest


class TestCRC64(unittest.TestCase):
    def test_positive_integer(self):
        result = CRC64.compute(123456789)
        expected = 0xA8E9F2D8578073DF  # Placeholder, replace with actual expected value
        self.assertEqual(result, expected)

    def test_negative_integer(self):
        result = CRC64.compute(-123456789)
        expected = 0x6BCD5C4AAB6E5F37  # Placeholder, replace with actual expected value
        self.assertEqual(result, expected)

    def test_zero(self):
        result = CRC64.compute(0)
        expected = 0x8B79EAEAC6D660F1  # Placeholder, replace with actual expected value
        self.assertEqual(result, expected)

    def test_maximum_unsigned_integer(self):
        result = CRC64.compute(0xFFFFFFFFFFFFFFFF)
        expected = 0xE9C6D914C4B8D9CA  # Placeholder, replace with actual expected value
        self.assertEqual(result, expected)

    def test_sequential_bytes(self):
        result = CRC64.compute(0x0102030405060708)
        expected = 0xD9963A56A1125ACB  # Placeholder, replace with actual expected value
        self.assertEqual(result, expected)
import ctypes

class CRC64:
    """
    A Python class to compute the CRC64 checksum using the polynomial 0xC96C5795D7870F42.
    This implementation utilizes the ctypes library to handle data as unsigned 64-bit integers.
    """

    POLY64REV = 0xC96C5795D7870F42  # The reverse polynomial used in the CRC computation.
    crc64_tab = []  # Static table used for the CRC computation.

    @classmethod
    def crc64_init_table(cls):
        """
        Initializes the CRC64 table for fast lookup. This table is used to speed up the calculation
        of CRC by using precomputed results of possible byte-wise CRC values.
        """
        if not cls.crc64_tab:
            # Only initialize the table if it has not been initialized yet
            for b in range(256):
                crc = ctypes.c_uint64(b).value  # Start with the byte value, treated as a 64-bit unsigned int
                for _ in range(8):
                    # Process each bit to determine CRC for a single byte
                    if crc & 1:
                        # If the least significant bit is 1, apply the polynomial
                        crc = (crc >> 1) ^ cls.POLY64REV
                    else:
                        # Otherwise, just shift right
                        crc >>= 1
                cls.crc64_tab.append(ctypes.c_uint64(crc).value)  # Store computed CRC in the table

    @staticmethod
    def crc64_update(crc, byte):
        """
        Updates the CRC value with a new byte using the CRC64 table.

        Args:
        crc : int
            Current CRC value.
        byte : int
            The next byte to be processed.

        Returns:
        int
            Updated CRC value.
        """
        tbl_idx = (crc ^ byte) & 0xFF  # Determine the table index
        # Update the CRC value by looking up the table and shifting the existing CRC
        return (CRC64.crc64_tab[tbl_idx] ^ (crc >> 8)) & 0xFFFFFFFFFFFFFFFF

    @classmethod
    def compute(cls, input_integer):
        """
        Computes the CRC64 checksum for an 8-byte integer.

        Args:
        input_integer : int
            Integer to compute the CRC64 checksum for. If negative, it's handled as a signed 64-bit integer.

        Returns:
        int
            Computed CRC64 checksum.
        """
        cls.crc64_init_table()  # Ensure the table is initialized

        # Handle negative integers by treating them as 64-bit unsigned integers
        if input_integer < 0:
            input_integer = (1 << 64) + input_integer

        crc = 0xFFFFFFFFFFFFFFFF  # Initial CRC value
        input_bytes = input_integer.to_bytes(8, 'little')  # Convert integer to bytes in little-endian format

        for b in input_bytes:
            crc = cls.crc64_update(crc, b)  # Update the CRC for each byte

        return crc ^ 0xFFFFFFFFFFFFFFFF  # Finalize the CRC computation