function findLongestNonDecreasingSubsequence(nums: number[]): number[] {
    const dp: number[][] = nums.map(() => []);
    const prev: number[][] = nums.map(() => []);

    let maxLength = 1;
    let maxIndex = 0;

    for (let i = 0; i < nums.length; i++) {
        dp[i].push(nums[i]);
        prev[i].push(-1);

        for (let j = 0; j < i; j++) {
            if (nums[i] >= nums[j] && dp[i].length < dp[j].length + 1) {
                dp[i] = [...dp[j], nums[i]];
                prev[i] = [...prev[j], j];
            }
        }

        if (dp[i].length > maxLength) {
            maxLength = dp[i].length;
            maxIndex = i;
        }
    }

    const result: number[] = [];
    let k = maxIndex;
    while (k !== -1) {
        result.unshift(nums[k]);
        k = prev[k][0];
    }

    return result;
}
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
