describe('compareArrays', () => {
    test('should return true for identical arrays with same order', () => {
        const arr1 = [1, 2, 3];
        const arr2 = [1, 2, 3];
        expect(compareArrays(arr1, arr2)).toBe(true);
    });

    test('should return true for identical arrays with different order', () => {
        const arr1 = [3, 2, 1];
        const arr2 = [1, 2, 3];
        expect(compareArrays(arr1, arr2)).toBe(true);
    });

    test('should return false for arrays with different elements', () => {
        const arr1 = [1, 2, 3];
        const arr2 = [4, 5, 6];
        expect(compareArrays(arr1, arr2)).toBe(false);
    });

    test('should return false for arrays with different lengths', () => {
        const arr1 = [1, 2, 3];
        const arr2 = [1, 2];
        expect(compareArrays(arr1, arr2)).toBe(false);
    });

    test('should return true for arrays with duplicate elements but same unique set', () => {
        const arr1 = [1, 1, 2, 3, 3];
        const arr2 = [3, 2, 1, 1];
        expect(compareArrays(arr1, arr2)).toBe(true);
    });
});