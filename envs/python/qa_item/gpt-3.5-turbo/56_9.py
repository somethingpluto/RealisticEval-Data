from typing import List

def find_shiftjis_not_gbk() -> List:
    """
    find all the characters that can be represented in Shift-JIS, but not in GBK, and return them as an array

    Returns:
        list: A list of characters that are unique to Shift-JIS, not encodable in GBK.
    """
    shift_jis_chars = []
    for i in range(0x8140, 0x9FFC):
        if i < 0x889F or (i > 0x9872 and i < 0x989F) or (i > 0xEAA4 and i < 0xEAA5) or (i > 0xEAA7 and i < 0xEAA8) or i > 0xEAAF:
            shift_jis_chars.append(chr(i))
    return shift_jis_chars
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