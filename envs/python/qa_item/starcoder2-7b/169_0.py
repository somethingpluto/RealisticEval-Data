def convert_to_roman(num: int) -> str:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
import unittest


class TestConvertToRoman(unittest.TestCase):
    def test_typical_number(self):
        result = convert_to_roman(1987)
        self.assertEqual(result, 'MCMLXXXVII')  # 1987 = M + CM + LXXX + VII

    def test_minimum_value(self):
        result = convert_to_roman(1)
        self.assertEqual(result, 'I')  # 1 = I

    def test_large_number(self):
        result = convert_to_roman(3999)
        self.assertEqual(result, 'MMMCMXCIX')  # 3999 = MMM + CM + XC + IX

    def test_different_numeral_repeats(self):
        result = convert_to_roman(1666)
        self.assertEqual(result, 'MDCLXVI')  # 1666 = M + D + CLX + VI

    def test_no_fives_and_ones(self):
        result = convert_to_roman(2000)
        self.assertEqual(result, 'MM')  # 2000 = MM

if __name__ == '__main__':
    unittest.main()