describe('lengthOfLIS', () => {
    test('should return 4 for input [10, 9, 2, 5, 3, 7, 101, 18]', () => {
        expect(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])).toBe(4);
    });

    test('should return 1 for input [1]', () => {
        expect(lengthOfLIS([1])).toBe(1);
    });

    test('should return 0 for input []', () => {
        expect(lengthOfLIS([])).toBe(0);
    });

    test('should return 5 for input [0, 1, 0, 3, 2, 3]', () => {
        expect(lengthOfLIS([0, 1, 0, 3, 2, 3])).toBe(4);
    });
});