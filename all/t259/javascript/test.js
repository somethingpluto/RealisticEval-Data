describe('isCompliantFourDigit', () => {
    describe('test positive four-digit number', () => {
        it('should return true for a standard positive four-digit number', () => {
            expect(isCompliantFourDigit(1234)).toBe(true);
        });
    });

    describe('test boundary values', () => {
        it('should return true for the lower boundary value', () => {
            expect(isCompliantFourDigit(1000)).toBe(true);
        });

        it('should return true for the upper boundary value', () => {
            expect(isCompliantFourDigit(9999)).toBe(true);
        });
    });

    describe('test negative four-digit number', () => {
        it('should return false for a negative four-digit number', () => {
            expect(isCompliantFourDigit(-1234)).toBe(false);
        });
    });

    describe('test out-of-range numbers', () => {
        it('should return false for a number below the range', () => {
            expect(isCompliantFourDigit(999)).toBe(false);
        });

        it('should return false for a number above the range', () => {
            expect(isCompliantFourDigit(10000)).toBe(false);
        });
    });
});