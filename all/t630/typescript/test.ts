describe('insertionSort', () => {
    test('Basic unsorted array', () => {
        const arr: number[] = [12.4, 11.2, 13.5, 5.6, 6.7];
        const expected: number[] = [5.6, 6.7, 11.2, 12.4, 13.5];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Already sorted array', () => {
        const arr: number[] = [1.1, 2.2, 3.3, 4.4, 5.5];
        const expected: number[] = [1.1, 2.2, 3.3, 4.4, 5.5];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Reverse sorted array', () => {
        const arr: number[] = [5.5, 4.4, 3.3, 2.2, 1.1];
        const expected: number[] = [1.1, 2.2, 3.3, 4.4, 5.5];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Empty array', () => {
        const arr: number[] = [];
        const expected: number[] = [];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Single element array', () => {
        const arr: number[] = [3.3];
        const expected: number[] = [3.3];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Array with duplicates', () => {
        const arr: number[] = [2.2, 3.3, 2.2, 1.1, 3.3];
        const expected: number[] = [1.1, 2.2, 2.2, 3.3, 3.3];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });

    test('Large numbers', () => {
        const arr: number[] = [1e10, 1e9, 1e11, 1e8];
        const expected: number[] = [1e8, 1e9, 1e10, 1e11];
        insertionSort(arr);
        expect(arr).toEqual(expected);
    });
});