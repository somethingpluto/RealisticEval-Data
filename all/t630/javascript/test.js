describe('insertionSort', () => {
    test('Test case 1: Basic unsorted array.', () => {
        const arr = [12.4, 11.2, 13.5, 5.6, 6.7];
        const expected = [5.6, 6.7, 11.2, 12.4, 13.5];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Test case 2: Already sorted array.', () => {
        const arr = [1.1, 2.2, 3.3, 4.4, 5.5];
        const expected = [1.1, 2.2, 3.3, 4.4, 5.5];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Test case 3: Reverse sorted array.', () => {
        const arr = [5.5, 4.4, 3.3, 2.2, 1.1];
        const expected = [1.1, 2.2, 3.3, 4.4, 5.5];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Test case 4: Empty array.', () => {
        const arr = [];
        const expected = [];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Test case 5: Single element array.', () => {
        const arr = [3.3];
        const expected = [3.3];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Test case 6: Array with duplicate values.', () => {
        const arr = [2.2, 3.3, 2.2, 1.1, 3.3];
        const expected = [1.1, 2.2, 2.2, 3.3, 3.3];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Test case 7: Large numbers.', () => {
        const arr = [1e10, 1e9, 1e11, 1e8];
        const expected = [1e8, 1e9, 1e10, 1e11];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });
});