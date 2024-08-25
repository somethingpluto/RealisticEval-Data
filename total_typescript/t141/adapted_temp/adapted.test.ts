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
function compareArrays<T>(arr1: Array<T>, arr2: Array<T>): boolean {

    // Create sets from both arrays to eliminate duplicates and enable fast lookup
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);

    // If the sizes of the sets are different, the arrays can't contain the same elements
    if (set1.size !== set2.size) {
        return false;
    }

    // Check if all elements in set1 are present in set2
    // @ts-ignore
    for (const item of set1) {
        if (!set2.has(item)) {
            return false;
        }
    }

    // If all checks passed, the arrays contain the same elements
    return true;
}