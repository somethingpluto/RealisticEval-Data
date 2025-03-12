
def format_bytes(bytes: int, options: dict = None) -> str:
    """
    Formats a given number of bytes into a human-readable string representation,
    using either the SI (decimal) or binary (accurate) size notation.

    Args:
        bytes (int): The number of bytes to format.
        options (dict, optional): Optional settings to customize the output.
            - 'decimals' (int): Number of decimal places to include in the result.
            -'sizeType' (str): Specifies whether to use binary ("accurate") or
              decimal ("normal") units.
              "accurate" uses units like KiB, MiB (base 1024).
              "normal" uses units like KB, MB (base 1000).

    Returns:
        str: A string representation of the byte size in a human-readable format.
    """
    if options is None:
        options = {}
    
    if options.get('decimals') is not None:
        decimals = options.get('decimals')
    elif decimals is None:
        decimals = 0
    else:
        decimals = int(decimals)
    
    if options.get('sizeType') is not None:
        sizeType = options.get('sizeType')
    elif sizeType is None:
        sizeType = 'accurate'
    else:
        sizeType = str(sizeType)
    
    if bytes < 1:
        return f"{sizeType} bytes ({bytes/1e3:.2f})"
    elif bytes < 1024:
        return f"{sizeType} KiB ({bytes/1e6:.2f})"
    elif bytes < 1048576:
        return f"{sizeType} MiB ({bytes/1e9:.2f})"
    else:
        return f"{sizeType} KB ({bytes/1024:.2f})"

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