describe('getIndexValues', () => {
    test('should return the index of the minimum value in an array', () => {
        const inputArray = [3, 1, 4, 1, 5, 9, 2];
        const result = getIndexValues(inputArray, compareMin);
        expect(result).toEqual([[1, 1], [3, 1]]);
    });

    test('should return the index of the maximum value in an array', () => {
        const inputArray = [3, 1, 4, 1, 5, 9, 2];
        const result = getIndexValues(inputArray, compareMax);
        expect(result).toEqual([[5, 9]]);
    });

    test('should return multiple indices if there are multiple minimum values', () => {
        const inputArray = [7, 5, 2, 2, 8];
        const result = getMinIndex(inputArray);
        expect(result).toEqual([[2, 2], [3, 2]]);
    });

    test('should return multiple indices if there are multiple maximum values', () => {
        const inputArray = [10, 4, 10, 1];
        const result = getMaxIndex(inputArray);
        expect(result).toEqual([[0, 10], [2, 10]]);
    });

    test('should return the index of the minimum value when array contains negative numbers', () => {
        const inputArray = [-3, -1, -7, -1, -5];
        const result = getMinIndex(inputArray);
        expect(result).toEqual([[2, -7]]);
    });
});