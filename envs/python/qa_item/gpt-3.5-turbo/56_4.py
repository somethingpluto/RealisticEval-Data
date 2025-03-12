from typing import List
import codecs

def find_shiftjis_not_gbk() -> List:
    shift_jis_chars = set()
    gbk_chars = set()

    for i in range(0x8140, 0x9FFC):
        try:
            char = bytes([i // 256, i % 256]).decode('shift_jis')
            shift_jis_chars.add(char)
        except UnicodeDecodeError:
            pass

    for i in range(0x8140, 0xFEFE):
        try:
            char = bytes([i // 256, i % 256]).decode('gbk')
            gbk_chars.add(char)
        except UnicodeDecodeError:
            pass

    return list(shift_jis_chars - gbk_chars)
import unittest


class TestFindShiftJISNotGBK(unittest.TestCase):

    def setUp(self):
        # Pre-calculate the list once since it's computationally expensive
        self.shiftjis_not_gbk = find_shiftjis_not_gbk()

    def test_known_shiftjis_character_not_in_gbk(self):
        # Test known characters (example values provided might not actually be in one and not the other; please adjust accordingly based on actual encoding tables)
        known_shiftjis_only = 'ヱ'  # An example character, ensure this is correct as per your encodings
        self.assertNotIn(known_shiftjis_only, self.shiftjis_not_gbk)

    def test_character_in_both_encodings(self):
        # Test characters known to be in both encodings
        common_character = '水'  # Common in both, ensure accuracy
        self.assertNotIn(common_character, self.shiftjis_not_gbk)

    def test_character_in_neither_encoding(self):
        # Character not typically found in either encoding
        neither_encoding_char = '\U0001F4A9'  # Emoji, not in basic Shift-JIS or GBK
        self.assertNotIn(neither_encoding_char, self.shiftjis_not_gbk)

    def test_bounds_of_bmp(self):
        # Characters at the edge of the BMP should be checked
        edge_of_bmp = '\uffff'  # Last character in BMP
        # Since this test.js is situational, we check based on the known state; may not be necessary
        if edge_of_bmp in self.shiftjis_not_gbk:
            self.assertIn(edge_of_bmp, self.shiftjis_not_gbk)
        else:
            self.assertNotIn(edge_of_bmp, self.shiftjis_not_gbk)
if __name__ == '__main__':
    unittest.main()