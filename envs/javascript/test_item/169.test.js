/**
 * Converts an Arabic numeral to its Roman numeral equivalent.
 *
 * @param {number} num - The number to convert.
 * @returns {string} The Roman numeral representation of the input number.
 */
function convertToRoman(num) {
    const romanNumerals = [
        { value: 1000, symbol: 'M' },
        { value: 900, symbol: 'CM' },
        { value: 500, symbol: 'D' },
        { value: 400, symbol: 'CD' },
        { value: 100, symbol: 'C' },
        { value: 90, symbol: 'XC' },
        { value: 50, symbol: 'L' },
        { value: 40, symbol: 'XL' },
        { value: 10, symbol: 'X' },
        { value: 9, symbol: 'IX' },
        { value: 5, symbol: 'V' },
        { value: 4, symbol: 'IV' },
        { value: 1, symbol: 'I' }
    ];

    let result = '';
    for (let i = 0; i < romanNumerals.length; i++) {
        while (num >= romanNumerals[i].value) {
            result += romanNumerals[i].symbol;
            num -= romanNumerals[i].value;
        }
    }
    return result;
}
describe('convertToRoman', () => {
    test('should return the correct Roman numeral for a typical number', () => {
        const result = convertToRoman(1987);
        expect(result).toBe('MCMLXXXVII'); // 1987 = M + CM + LXXX + VII
    });

    test('should return the correct Roman numeral for the minimum value (1)', () => {
        const result = convertToRoman(1);
        expect(result).toBe('I'); // 1 = I
    });

    test('should return the correct Roman numeral for a large number (3999)', () => {
        const result = convertToRoman(3999);
        expect(result).toBe('MMMCMXCIX'); // 3999 = MMM + CM + XC + IX
    });

    test('should return the correct Roman numeral for a number with different numeral repeats', () => {
        const result = convertToRoman(1666);
        expect(result).toBe('MDCLXVI'); // 1666 = M + D + CLX + VI
    });

    test('should return the correct Roman numeral for number with no 5s and 1s', () => {
        const result = convertToRoman(2000);
        expect(result).toBe('MM'); // 2000 = MM
    });
});
