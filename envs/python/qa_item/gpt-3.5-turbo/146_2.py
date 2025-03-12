import math

def format_bytes(bytes: int, options: dict = None) -> str:
    if options is None:
        options = {'decimals': 2, 'sizeType': 'normal'}
    
    decimals = options.get('decimals', 2)
    size_type = options.get('sizeType', 'normal')
    
    base = 1000 if size_type == 'normal' else 1024
    
    if bytes == 0:
        return '0 Bytes'
    
    size_name = ('Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    i = int(math.floor(math.log(bytes) / math.log(base)))
    formatted_bytes = round(bytes / math.pow(base, i), decimals)
    
    return f'{formatted_bytes} {size_name[i]}'
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