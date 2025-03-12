import { isEqual } from 'lodash';

function safeSplice<T>(
    inputArray: T[],
    amountToRemove: number,
    indexToRemove: number,
    replaceWith?: T
): T[] {
    if (indexToRemove < 0 || indexToRemove >= inputArray.length) {
        throw new Error('Index out of bounds');
    }
    if (amountToRemove < 0 || indexToRemove + amountToRemove > inputArray.length) {
        throw new Error('Invalid amount to remove');
    }
    const result = [...inputArray];
    // ... rest of the function remains unchanged
    if (replaceWith !== undefined) {
        result.splice(indexToRemove, amountToRemove, replaceWith);
    }
    return result;
}
describe('safeSplice', () => {
    test('replaces removed elements with a new element', () => {
        const inputArray: string[] = ['a', 'b', 'c', 'd', 'e'];
        const expected: string[] = ['a', 'z', 'e'];
        expect(safeSplice(inputArray, 3, 1, 'z')).toEqual(expected);
    });

    test('should remove specified elements and replace with new element', () => {
        const inputArray: number[] = [1, 2, 3, 4, 5];
        const amountToRemove: number = 2;
        const indexToRemove: number = 1;
        const replaceWith: number = 99;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        expect(result).toEqual([1, 99, 4, 5]);
    });

    test('should handle removing elements from the end of the array', () => {
        const inputArray: number[] = [1, 2, 3, 4, 5];
        const amountToRemove: number = 2;
        const indexToRemove: number = 3;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove);
        expect(result).toEqual([1, 2, 3]);
    });

    test('should handle the case where no elements are removed', () => {
        const inputArray: number[] = [1, 2, 3, 4, 5];
        const amountToRemove: number = 0;
        const indexToRemove: number = 2;
        const replaceWith: number = 99;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        expect(result).toEqual([1, 2, 99, 3, 4, 5]);
    });

    test('should handle edge case with an empty input array', () => {
        const inputArray: number[] = [];
        const amountToRemove: number = 1;
        const indexToRemove: number = 0;
        const replaceWith: number = 99;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        expect(result).toEqual([99]);
    });
});
