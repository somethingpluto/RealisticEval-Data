describe('TestAnswer', () => {
    test('non-decreasing sequence', () => {
        const nums = [5, 7, 4, 8, 6, 10, 2, 11];
        const expected = [5, 7, 8, 10, 11];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('all increasing', () => {
        const nums = [1, 2, 3, 4, 5];
        const expected = [1, 2, 3, 4, 5];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('all decreasing', () => {
        const nums = [5, 4, 3, 2, 1];
        const expected = [5];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('single element', () => {
        const nums = [10];
        const expected = [10];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('empty array', () => {
        const nums = [];
        const expected = [];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });
});