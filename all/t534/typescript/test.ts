describe('removeElementInArray', () => {
    test('returns the original array when the element is not found', () => {
        const result = removeElementInArray([1, 2, 3, 4], 5);
        expect(result).toEqual([1, 2, 3, 4]);
    });

    test('handles an empty array correctly', () => {
        const result = removeElementInArray([], 1);
        expect(result).toEqual([]);
    });

    test('removes an element from an array of objects', () => {
        const obj1 = { id: 1 };
        const obj2 = { id: 2 };
        const obj3 = { id: 3 };
        const result = removeElementInArray([obj1, obj2, obj3], obj2);
        expect(result).toEqual([obj1, obj3]);
    });

    test('does not modify the original array', () => {
        const originalArray = [1, 2, 3];
        const result = removeElementInArray(originalArray, 2);
        expect(originalArray).toEqual([1, 2, 3]);
        expect(result).toEqual([1, 3]);
    });
});