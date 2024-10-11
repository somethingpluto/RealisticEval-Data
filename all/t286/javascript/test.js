describe('findLargestDivisible', () => {
    it('should return null when there is no number between n and half of n that is divisible by 5 or 10', () => {
        expect(findLargestDivisible(2)).toBeNull();
        expect(findLargestDivisible(3)).toBeNull();
        expect(findLargestDivisible(4)).toBeNull();
    });

    it('should return the largest number between n and half of n that is divisible by 5 or 10', () => {
        expect(findLargestDivisible(10)).toBe(10);
        expect(findLargestDivisible(15)).toBe(15);
        expect(findLargestDivisible(20)).toBe(20);
        expect(findLargestDivisible(25)).toBe(25);
        expect(findLargestDivisible(26)).toBe(25);
        expect(findLargestDivisible(75)).toBe(75);
    });
});