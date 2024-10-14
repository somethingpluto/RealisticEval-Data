describe('TestFindClosestElement', () => {
    it('should return 3 as it is the first closest element to 5', () => {
        expect(findClosestElement(5, [1, 3, 7, 8, 9])).toBe(3);
    });

    it('should return 7 as it exactly matches the target', () => {
        expect(findClosestElement(7, [1, 3, 7, 8, 9])).toBe(7);
    });

    it('should return 4 as it is the first closest element to 5', () => {
        expect(findClosestElement(5, [4, 6, 8, 9])).toBe(4);
    });

    it('should return 3.3 as it is the first closest element to 5.5', () => {
        expect(findClosestElement(5.5, [1.1, 3.3, 7.7, 8.8])).toBe(3.3);
    });
});