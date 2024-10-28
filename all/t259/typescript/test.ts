describe('isCompliantFourDigit', () => {
    it('should return true for a standard positive four-digit number', () => {
        expect(isCompliantFourDigit(1234)).toBe(true);
    });

    it('should return true for boundary values of the range', () => {
        expect(isCompliantFourDigit(1000)).toBe(true);
        expect(isCompliantFourDigit(9999)).toBe(true);
    });

    it('should return false for a negative four-digit number', () => {
        expect(isCompliantFourDigit(-1234)).toBe(false);
    });

    it('should return false for numbers that are out of the four-digit range', () => {
        expect(isCompliantFourDigit(999)).toBe(false);
        expect(isCompliantFourDigit(10000)).toBe(false);
    });
});