describe('isCompliantFourDigit', () => {
    it('should return true for a four-digit number', () => {
        expect(isCompliantFourDigit(1234)).toBe(true);
    });

    it('should return false for a number less than 1000', () => {
        expect(isCompliantFourDigit(999)).toBe(false);
    });

    it('should return false for a number greater than 9999', () => {
        expect(isCompliantFourDigit(10000)).toBe(false);
    });

    it('should return false for a non-integer', () => {
        expect(() => isCompliantFourDigit(123.45)).toThrowError('number must be an integer');
    });
});