SI_UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
BINARY_UNITS = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']

def format_bytes(bytes: int, options: dict = None) -> str:
    if options is None:
        options = {'decimals': 2,'sizeType': 'normal'}

    size_type = options.get('sizeType', 'normal')
    decimals = options.get('decimals', 2)

    if size_type == 'binary':
        units = BINARY_UNITS
    else:
        units = SI_UNITS

    magnitude = 0
    while bytes >= 1024:
        bytes /= 1024
        magnitude += 1

    power = 3 * magnitude
    formatted_bytes = round(bytes, decimals)
    return f"{formatted_bytes} {units[magnitude if size_type == 'binary' else power]}"
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