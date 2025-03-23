def check(candidate):

    # Check some simple cases
    assert candidate(19) == 'xix'
    assert candidate(152) == 'clii'
    assert candidate(251) == 'ccli'
    assert candidate(426) == 'cdxxvi'
    assert candidate(500) == 'd'
    assert candidate(1) == 'i'
    assert candidate(4) == 'iv'
    assert candidate(43) == 'xliii'
    assert candidate(90) == 'xc'
    assert candidate(94) == 'xciv'
    assert candidate(532) == 'dxxxii'
    assert candidate(900) == 'cm'
    assert candidate(994) == 'cmxciv'
    assert candidate(1000) == 'm'

    # Check some edge cases that are easy to work out by hand.
    assert True

def int_to_mini_roman(number):
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    def single_digit(n):
        if n == 1:
            return 'I'
        elif n == 2:
            return 'II'
        elif n == 3:
            return 'III'
        elif n == 4:
            return 'IV'
        elif n == 5:
            return 'V'
        elif n == 6:
            return 'VI'
        elif n == 7:
            return 'VII'
        elif n == 8:
            return 'VIII'
        elif n == 9:
            return 'IX'

    def convert_number(number):
        result = ''
        for i in range(len(str(number))):
            current_digit = int(str(number)[i])
            next_digit = int(str(number)[i + 1]) if i < len(str(number)) - 1 else 0

            if current_digit >= next_digit:
                result += roman_dict[list(roman_dict.keys())[current_digit - 1]]
            else:
                if current_digit - next_digit == 4:
                    result += roman_dict[list(roman_dict.keys())[current_digit - 5]] + roman_dict[list(roman_dict.keys())[current_digit - 1]]
                elif current_digit - next_digit == 9:
                    result += roman_dict[list(roman_dict.keys())[current_digit - 10]] + roman_dict[list(roman_dict.keys())[current_digit - 1]]

        return result

    return convert_number(number)
candidate = int_to_mini_roman
check(candidate)