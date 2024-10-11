describe('findLargestDivisible', () => {
    it('should return the largest number divisible by 5 or 10', () => {
        expect(findLargestDivisible(30)).toBe(30);
        expect(findLargestDivisible(29)).toBe(25);
        expect(findLargestDivisible(10)).toBe(10);
        expect(findLargestDivisible(5)).toBe(5);
        expect(findLargestDivisible(4)).toBe(null);
    });

    it('should handle edge cases correctly', () => {
        expect(findLargestDivisible(0)).toBe(null);
        expect(findLargestDivisible(-10)).toBe(null);
        expect(findLargestDivisible(1)).toBe(null);
    });
});