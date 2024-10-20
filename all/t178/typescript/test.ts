describe('TestAnswer', () => {
    test('non-decreasing sequence', () => {
        const nums: number[] = [5, 7, 4, 8, 6, 10, 2, 11];
        const expected: number[] = [5, 7, 8, 10, 11];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('all increasing', () => {
        const nums: number[] = [1, 2, 3, 4, 5];
        const expected: number[] = [1, 2, 3, 4, 5];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('all decreasing', () => {
        const nums: number[] = [5, 4, 3, 2, 1];
        const expected: number[] = [5];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('single element', () => {
        const nums: number[] = [10];
        const expected: number[] = [10];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('empty array', () => {
        const nums: number[] = [];
        const expected: number[] = [];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });
});