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