import unittest

class Tester(unittest.TestCase):
    def test_valid_hex_string_1(self):
        self.assertEqual(hex_string_to_unsigned_int("1A3F"), 6719)  # 1A3F in hex is 6719 in decimal

    def test_valid_hex_string_2(self):
        self.assertEqual(hex_string_to_unsigned_int("FFFF"), 65535)  # FFFF in hex is 65535 in decimal

    def test_valid_hex_string_3(self):
        self.assertEqual(hex_string_to_unsigned_int("0"), 0)  # 0 in hex is 0 in decimal

    def test_valid_hex_string_4(self):
        self.assertEqual(hex_string_to_unsigned_int("7F"), 127)  # 7F in hex is 127 in decimal

    def test_valid_hex_string_5(self):
        self.assertEqual(hex_string_to_unsigned_int("ABC123"), 11256099)  # ABC123 in hex is 11256099 in decimal

    def test_lowercase_hex_string(self):
        self.assertEqual(hex_string_to_unsigned_int("abcd"), 43981)  # abcd in hex is 43981 in decimal

    def test_hex_string_with_leading_zeroes(self):
        self.assertEqual(hex_string_to_unsigned_int("0001"), 1)  # 0001 in hex is 1 in decimal

    def test_mixed_case_hex_string(self):
        self.assertEqual(hex_string_to_unsigned_int("AbCdEf"), 11259375)  # AbCdEf in hex is 11259375 in decimal