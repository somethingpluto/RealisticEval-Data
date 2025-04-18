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