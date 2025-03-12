def format_bytes(bytes: int, options: dict = None) -> str:
    if options is None:
        options = {}

    decimals = options.get('decimals', 2)
    size_type = options.get('sizeType', 'accurate')

    if size_type == 'accurate':
        sizes = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
        base = 1024
    else:
        sizes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
        base = 1000

    if bytes < base:
        return f"{bytes} {sizes[0]}"

    for i in range(1, len(sizes)):
        if bytes < base ** i:
            return f"{bytes / (base ** (i - 1)):.{decimals}f} {sizes[i - 1]}"

    return f"{bytes / (base ** (len(sizes) - 1)):.{decimals}f} {sizes[-1]}"
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