/**
 * Convert Arabic digits in the string to corresponding English digits
 * @param {string} str - The input string containing Arabic digits
 * @returns {string} - The string with Arabic digits replaced by English digits
 */
function arabicToEnglishNumbers(str) {
  // Mapping of Arabic digits to English digits
  const arabicToEnglish = {
    '٠': '0',
    '١': '1',
    '٢': '2',
    '٣': '3',
    '٤': '4',
    '٥': '5',
    '٦': '6',
    '٧': '7',
    '٨': '8',
    '٩': '9'
  };

  // Replace Arabic digits with English digits
  return str.replace(/[٠١٢٣٤٥٦٧٨٩]/g, function(match) {
    return arabicToEnglish[match];
  });
}
describe('arabicToEnglishNumbers', () => {
    test('should convert Arabic numerals to English numerals', () => {
        const input = "١٢٣٤٥٦٧٨٩٠";
        const expectedOutput = "1234567890";
        expect(arabicToEnglishNumbers(input)).toBe(expectedOutput);
    });

    test('should return the same string if there are no Arabic numerals', () => {
        const input = "Hello, World!";
        const expectedOutput = "Hello, World!";
        expect(arabicToEnglishNumbers(input)).toBe(expectedOutput);
    });

    test('should handle a mix of Arabic numerals and English characters', () => {
        const input = "رقم ١٢٣ هو المثال";
        const expectedOutput = "رقم 123 هو المثال";
        expect(arabicToEnglishNumbers(input)).toBe(expectedOutput);
    });

    test('should handle empty string', () => {
        const input = "";
        const expectedOutput = "";
        expect(arabicToEnglishNumbers(input)).toBe(expectedOutput);
    });

    test('should handle a string with mixed Arabic and English numerals', () => {
        const input = "The number is ٣٥٦ and 789.";
        const expectedOutput = "The number is 356 and 789.";
        expect(arabicToEnglishNumbers(input)).toBe(expectedOutput);
    });
});
