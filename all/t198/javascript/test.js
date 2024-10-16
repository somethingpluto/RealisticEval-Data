describe('findMaxDifference', () => {
    test('General case', () => {
        const l = [2, 3, 10, 6, 4, 8, 1];
        expect(findMaxDifference(l)).toBe(8);  // Maximum difference is 10 - 2 = 8
    });

    test('Decreasing sequence', () => {
        const l = [10, 9, 8, 7, 6, 5];
        expect(findMaxDifference(l)).toBe(0);  // Maximum difference should be 0, as all differences are negative
    });

    test('All elements the same', () => {
        const l = [5, 5, 5, 5, 5];
        expect(findMaxDifference(l)).toBe(0);  // Maximum difference is 5 - 5 = 0
    });

    test('Only two elements', () => {
        const l = [3, 8];
        expect(findMaxDifference(l)).toBe(5);  // Maximum difference is 8 - 3 = 5
    });

    test('Single element', () => {
        const l = [4];
        expect(findMaxDifference(l)).toBe(0);  // Only one element, no difference to calculate
    });
});