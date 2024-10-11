describe('lengthOfLIS', () => {
    it('should return 4 for [10,9,2,5,3,7,101,18]', () => {
        expect(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])).toBe(4);
    });

    it('should return 1 for [0]', () => {
        expect(lengthOfLIS([0])).toBe(1);
    });

    it('should return 1 for [1]', () => {
        expect(lengthOfLIS([1])).toBe(1);
    });

    it('should return 0 for []', () => {
        expect(lengthOfLIS([])).toBe(0);
    });
});