describe('findMaxDifference', () => {
    // Test case 1: General case
    test('General case', () => {
        const l: number[] = [2, 3, 10, 6, 4, 8, 1];
        expect(findMaxDifference(l)).toBe(8);  // Maximum difference is 10 - 2 = 8
    });

    // Test case 2: Decreasing sequence
    test('Decreasing sequence', () => {
        const l: number[] = [10, 9, 8, 7, 6, 5];
        expect(findMaxDifference(l)).toBe(0);  // Maximum difference should be 0, as all differences are negative
    });

    // Test case 3: All elements the same
    test('All elements the same', () => {
        const l: number[] = [5, 5, 5, 5, 5];
        expect(findMaxDifference(l)).toBe(0);  // Maximum difference is 5 - 5 = 0
    });

    // Test case 4: Only two elements
    test('Only two elements', () => {
        const l: number[] = [3, 8];
        expect(findMaxDifference(l)).toBe(5);  // Maximum difference is 8 - 3 = 5
    });

    // Test case 5: Only one element
    test('Single element', () => {
        const l: number[] = [4];
        expect(findMaxDifference(l)).toBe(0);  // Only one element, no difference to calculate
    });
});