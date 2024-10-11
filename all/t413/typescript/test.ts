describe('getPalindromeList', () => {
    it('should return an empty array for n = 0', () => {
        expect(getPalindromeList(0)).toEqual([]);
    });

    it('should return [1] for n = 1', () => {
        expect(getPalindromeList(1)).toEqual([1]);
    });

    it('should return [1, 2, 3] for n = 3', () => {
        expect(getPalindromeList(3)).toEqual([1, 2, 3]);
    });

    it('should return [1, 2, 3, 4, 5] for n = 5', () => {
        expect(getPalindromeList(5)).toEqual([1, 2, 3, 4, 5]);
    });

    it('should return [1, 2, 3, 4, 5, 6, 7, 8, 9] for n = 9', () => {
        expect(getPalindromeList(9)).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9]);
    });

    it('should return [1, 2, 3, 4, 5, 6, 7, 8, 9, 11] for n = 11', () => {
        expect(getPalindromeList(11)).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]);
    });
});