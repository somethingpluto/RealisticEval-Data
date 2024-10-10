describe('numericalStrConvert', () => {
    it('converts integer strings to integers', () => {
        expect(numericalStrConvert('123')).toBe(123);
    });

    it('converts floating point strings to floats', () => {
        expect(numericalStrConvert('123.45')).toBeCloseTo(123.45);
    });

    it('returns original string for non-numeric strings', () => {
        expect(numericalStrConvert('abc')).toBe('abc');
        expect(numericalStrConvert('hello world')).toBe('hello world');
    });
});