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

   test('should handle zero or negative values gracefully (edge case)', () => {
    expect(() => {
        convertToRoman(0);
    }).toThrowError('Input must be a positive integer');

    expect(() => {
        convertToRoman(-5);
    }).toThrowError('Input must be a positive integer');
    });

    test('should throw an error for non-integer input (exception case)', () => {
        expect(() => {
            convertToRoman(3.14);
        }).toThrowError('Input must be a positive integer');
    });

});
export function convertToRoman(num: number): string {
    if (!Number.isInteger(num) || num <= 0) {
        throw new Error('Input must be a positive integer');
    }

    const romanNumerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    const romanValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

    let result = "";

    for (let i = 0; i < romanNumerals.length; i++) {
        while (num >= romanValues[i]) {
            result += romanNumerals[i];
            num -= romanValues[i];
        }
    }

    return result;
}