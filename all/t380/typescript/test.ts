describe('calculateTotalSeconds', () => {
    it('should calculate total seconds correctly with all values provided', () => {
        expect(calculateTotalSeconds([1, 2, 3, 4])).toBe(93784);
    });

    it('should calculate total seconds correctly with some values missing', () => {
        expect(calculateTotalSeconds([0, 2, 3])).toBe(7380);
    });

    it('should handle default values when no arguments are provided', () => {
        expect(calculateTotalSeconds([])).toBe(0);
    });

    it('should handle default values when some arguments are missing', () => {
        expect(calculateTotalSeconds([1, undefined, undefined, 4])).toBe(90004);
    });
});