import math

def format_bytes(bytes: int, options: dict = None) -> str:
    """
    Formats a given number of bytes into a human-readable string representation,
    using either the SI (decimal) or binary (accurate) size notation.

    Args:
        bytes (int): The number of bytes to format.
        options (dict, optional): Optional settings to customize the output.
            - 'decimals' (int): Number of decimal places to include in the result.
            - 'sizeType' (str): Specifies whether to use binary ("accurate") or
              decimal ("normal") units.
              "accurate" uses units like KiB, MiB (base 1024).
              "normal" uses units like KB, MB (base 1000).

    Returns:
        str: A string representation of the byte size in a human-readable format.
    """
    if options is None:
        options = {}
    
    decimals = options.get('decimals', 2)
    size_type = options.get('sizeType', 'normal')
    
    if size_type == 'normal':
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
        base = 1000
    else:
        suffixes = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
        base = 1024
    
    if bytes == 0:
        return '0 ' + suffixes[0]
    
    exp = int(math.log(bytes, base))
    coefficient = bytes / (base ** exp)
    
    return f"{coefficient:.{decimals}f} {suffixes[exp]}"
import unittest

class TestFormatBytes(unittest.TestCase):

    def test_zero_bytes(self):
        result = format_bytes(0)
        self.assertIn(result, ['0 B', '0 Byte'])

    def test_two_kb(self):
        result = format_bytes(2048)
        self.assertIn(result, ['2 KB', '2.0 KB'])

    def test_two_kib(self):
        result = format_bytes(2048, {'sizeType': 'accurate'})
        self.assertIn(result, ['2 KiB', '2.0 KiB'])

    def test_five_mb(self):
        result = format_bytes(5242880)
        self.assertIn(result, ['5 MB', '5.0 MB'])

    def test_five_mib_with_decimals(self):
        result = format_bytes(5242880, {'decimals': 2, 'sizeType': 'accurate'})
        self.assertEqual(result, '5.00 MiB')
if __name__ == '__main__':
    unittest.main()