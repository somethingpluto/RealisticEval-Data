/**
 * Converts Arabic numerals in a string to English numerals.
 * This function iterates over each character in the input string, replacing Arabic numerals (٠-٩)
 * with their corresponding English numerals (0-9) while leaving other characters unchanged.
 *
 * @param {string} value - The string containing Arabic numerals to be converted.
 * @returns {string} The converted string with Arabic numerals replaced by English numerals.
 */
function arabicToEnglishNumbers(value) {
    const arabicNumerals = '٠١٢٣٤٥٦٧٨٩';
    const englishNumerals = '0123456789';

    return value.split('').map(char => {
        const index = arabicNumerals.indexOf(char);
        return index !== -1 ? englishNumerals[index] : char;
    }).join('');
}
describe('arabicToEnglishNumbers', () => {
    test('converts single Arabic numerals to English', () => {
        expect(arabicToEnglishNumbers('١')).toBe('1');
        expect(arabicToEnglishNumbers('٥')).toBe('5');
        expect(arabicToEnglishNumbers('٩')).toBe('9');
    });

    test('converts a string of Arabic numerals to English', () => {
        expect(arabicToEnglishNumbers('٠١٢٣٤٥٦٧٨٩')).toBe('0123456789');
    });

    test('handles strings with Arabic and English numerals mixed', () => {
        expect(arabicToEnglishNumbers('٠١23٤5')).toBe('012345');
    });

    test('leaves non-numeral characters unchanged', () => {
        expect(arabicToEnglishNumbers('Hello World!')).toBe('Hello World!');
        expect(arabicToEnglishNumbers('2022-٢٠٢٣')).toBe('2022-2023');
    });

    test('works with full sentences that include Arabic numerals', () => {
        expect(arabicToEnglishNumbers('The year is ٢٠٢٤!')).toBe('The year is 2024!');
    });

    test('handles empty strings correctly', () => {
        expect(arabicToEnglishNumbers('')).toBe('');
    });

    test('processes Arabic numerals in a complex mixed context', () => {
        expect(arabicToEnglishNumbers('Price: ٥٠٠$ and Date: ٢٠٢٣-١٢-٠١')).toBe('Price: 500$ and Date: 2023-12-01');
    });
});
