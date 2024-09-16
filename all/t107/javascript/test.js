describe('findMedian', () => {
    // Example usage with a large array
    test('should find the median of a large array with 10001 random elements', () => {
        const largeArray = Array.from({ length: 10001 }, () => Math.floor(Math.random() * 10000));
        const medianLargeArray = findMedian(largeArray);
        // It's difficult to assert the exact median here due to randomness,
        // but this test can check if the function completes without error
        expect(typeof medianLargeArray).toBe('number');
    });

    // Test Case 1: Odd number of elements
    test('should return 3 for an array with odd number of elements', () => {
        const arr1 = [3, 1, 4, 1, 5, 9, 2];
        const median1 = findMedian(arr1);
        expect(median1).toBe(3);
    });

    // Test Case 2: Even number of elements
    test('should return 6 for an array with even number of elements', () => {
        const arr2 = [10, 2, 3, 5, 7, 8];
        const median2 = findMedian(arr2);
        expect(median2).toBe(6);
    });

    // Test Case 3: Array with duplicate elements
    test('should return 2 for an array with duplicate elements', () => {
        const arr3 = [1, 2, 2, 2, 3];
        const median3 = findMedian(arr3);
        expect(median3).toBe(2);
    });

    // Test Case 4: Array with negative numbers
    test('should return 0 for an array with negative and positive numbers', () => {
        const arr4 = [-5, -10, 0, 5, 10];
        const median4 = findMedian(arr4);
        expect(median4).toBe(0);
    });

    // Test Case 5: Array with a single element
    test('should return the only element for an array with a single element', () => {
        const arr5 = [42];
        const median5 = findMedian(arr5);
        expect(median5).toBe(42);
    });
});