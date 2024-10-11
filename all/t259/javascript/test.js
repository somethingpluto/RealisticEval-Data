describe('isCompliantFourDigit', () => {
    it('should return true for a valid four-digit number', () => {
        expect(isCompliantFourDigit(1234)).toBe(true);
    });

    it('should return false for a three-digit number', () => {
        expect(isCompliantFourDigit(123)).toBe(false);
    });

    it('should return false for a five-digit number', () => {
        expect(isCompliantFourDigit(12345)).toBe(false);
    });

    it('should return false for a non-integer value', () => {
        expect(isCompliantFourDigit('1234')).toBe(false);
    });
});