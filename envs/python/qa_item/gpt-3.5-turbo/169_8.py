def convert_to_roman(num: int) -> str:
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    
    result = ''
    
    for value, numeral in roman_numerals.items():
        while num >= value:
            result += numeral
            num -= value
    
    return result
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