describe('safeSplice function tests', () => {
    test('should remove one element and replace it with another', () => {
        const result = safeSplice([1, 2, 3, 4, 5], 1, 2, 99);
        expect(result).toEqual([1, 99, 4, 5]);
    });

    test('should remove multiple elements and replace them with one element', () => {
        const result = safeSplice([10, 20, 30, 40, 50], 2, 1, 99);
        expect(result).toEqual([10, 20, 99, 40, 50]);
    });

    test('should remove elements without replacing', () => {
        const result = safeSplice([1, 2, 3, 4, 5], 2, 1);
        expect(result).toEqual([1, 2, 4, 5]);
    });

    test('should replace an element at the start of the array', () => {
        const result = safeSplice([1, 2, 3, 4, 5], 0, 0, 99);
        expect(result).toEqual([99, 1, 2, 3, 4, 5]);
    });

    test('should replace an element at the end of the array', () => {
        const result = safeSplice([1, 2, 3, 4, 5], 4, 1, 99);
        expect(result).toEqual([1, 2, 3, 4, 99]);
    });
});