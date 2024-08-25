import unittest


class TestGetFileSize(unittest.TestCase):

    def test_auto_unit_selection(self):
        """ Test automatic unit selection based on file size """
        # Test that units are correctly auto-selected based on size
        self.assertEqual(get_file_size(500), ('500 B', 500))  # Bytes
        self.assertEqual(get_file_size(2000), ('1.95 KB', 1.953125))  # Kilobytes
        self.assertEqual(get_file_size(3 * 1024 ** 2), ('3.00 MB', 3.0))  # Megabytes
        self.assertEqual(get_file_size(5 * 1024 ** 3), ('5.00 GB', 5.0))  # Gigabytes

    def test_specific_unit(self):
        """ Test output when specific units are requested """
        # Test for each unit conversion
        self.assertEqual(get_file_size(1024, 'KB'), ('1.00 KB', 1.0))

    def test_invalid_unit(self):
        """ Test behavior when an invalid unit is provided """
        with self.assertRaises(ValueError):
            get_file_size(1024, 'xyz')  # Should raise ValueError for invalid unit

    def test_large_file_size(self):
        """ Test with very large file size """
        # Testing a large number, should format to gigabytes
        self.assertEqual(get_file_size(10 * 1024 ** 4), ('10240.00 GB', 10240.0))

    def test_zero_bytes(self):
        """ Test with zero bytes """
        # Edge case for zero bytes
        self.assertEqual(get_file_size(0), ('0 B', 0))

def get_file_size(size_in_bytes, unit=None):
    """
    Converts a file size in bytes to a specified unit, or to an appropriately scaled unit if none is specified.

    Parameters:
    size_in_bytes (int): File size in bytes.
    unit (str, optional): The unit to convert the size to ('B', 'KB', 'MB', 'GB').

    Returns:
    tuple: A tuple containing the formatted size string and the size converted to the specified or chosen unit as float.
    """
    units = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3
    }

    if unit is None:
        # Automatically choose unit based on size
        if size_in_bytes < 1024:
            unit = 'B'
        elif size_in_bytes < 1024 ** 2:
            unit = 'KB'
        elif size_in_bytes < 1024 ** 3:
            unit = 'MB'
        else:
            unit = 'GB'
    else:
        unit = unit.upper()  # Normalize unit input to uppercase
        if unit not in units:
            raise ValueError("Invalid unit. Choose among 'B', 'KB', 'MB', 'GB'.")

    # Calculate the size in the chosen or specified unit
    size_in_unit = size_in_bytes / units[unit]

    # Format the size with two decimal places if not in bytes
    if unit == 'B':
        formatted_size = f"{size_in_bytes} B"
    else:
        formatted_size = f"{size_in_unit:.2f} {unit}"

    return formatted_size, size_in_unit
