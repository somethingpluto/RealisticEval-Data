describe('safeSplice', () => {
    test('replaces removed elements with a new element', () => {
        const inputArray = ['a', 'b', 'c', 'd', 'e'];
        const expected = ['a', 'z', 'e'];
        expect(safeSplice(inputArray, 3, 1, 'z')).toEqual(expected);
    });
    test('should remove specified elements and replace with new element', () => {
        const inputArray = [1, 2, 3, 4, 5];
        const amountToRemove = 2;
        const indexToRemove = 1;
        const replaceWith = 99;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        expect(result).toEqual([1, 99, 4, 5]);
    });

    test('should handle removing elements from the end of the array', () => {
        const inputArray = [1, 2, 3, 4, 5];
        const amountToRemove = 2;
        const indexToRemove = 3;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove);
        expect(result).toEqual([1, 2, 3]);
    });

    test('should handle the case where no elements are removed', () => {
        const inputArray = [1, 2, 3, 4, 5];
        const amountToRemove = 0;
        const indexToRemove = 2;
        const replaceWith = 99;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        expect(result).toEqual([1, 2, 99, 3, 4, 5]);
    });

    test('should handle edge case with an empty input array', () => {
        const inputArray = [];
        const amountToRemove = 1;
        const indexToRemove = 0;
        const replaceWith = 99;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        expect(result).toEqual([99]);
    });
});
