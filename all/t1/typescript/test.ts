describe('numericalStrConvert', () => {
    test('converts valid integers to numbers', () => {
        expect(numericalStrConvert('123')).toBe(123);
        expect(numericalStrConvert('-456')).toBe(-456);
    });

    test('converts valid floating-point numbers to numbers', () => {
        expect(numericalStrConvert('123.45')).toBeCloseTo(123.45);
        expect(numericalStrConvert('-456.78')).toBeCloseTo(-456.78);
    });

    test('returns original string for non-numeric values', () => {
        expect(numericalStrConvert('abc')).toBe('abc');
        expect(numericalStrConvert('hello world')).toBe('hello world');
    });
});