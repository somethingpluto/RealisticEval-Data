/**
 * Converts an Arabic numeral to its Roman numeral equivalent.
 *
 * @param {number} num - The number to convert.
 * @returns {string} The Roman numeral representation of the input number.
 */
function convertToRoman(num) {
    if (typeof num !== 'number' || num <= 0 || num >= 4000) {
        throw new Error('Input must be a number between 1 and 3999.');
    }

    const romanNumerals = [
        ['M', 1000],
        ['CM', 900],
        ['D', 500],
        ['CD', 400],
        ['C', 100],
        ['XC', 90],
        ['L', 50],
        ['XL', 40],
        ['X', 10],
        ['IX', 9],
        ['V', 5],
        ['IV', 4],
        ['I', 1]
    ];

    let result = '';

    for (let i = 0; i < romanNumerals.length; i++) {
        const [roman, value] = romanNumerals[i];
        while (num >= value) {
            result += roman;
            num -= value;
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
