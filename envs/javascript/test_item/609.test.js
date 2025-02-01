/**
 * Finds two indices of numbers in the array that sum up to the target value.
 *
 * @param {number[]} nums - The input array of integers.
 * @param {number} target - The target sum value.
 * @returns {number[]} A list containing the indices of the two numbers.
 * @throws {Error} If no such indices are found.
 */
function twoSum(nums, target) {
    const numMap = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (numMap.has(complement)) {
            return [numMap.get(complement), i];
        }
        numMap.set(nums[i], i);
    }
    throw new Error('No two sum solution');
}
describe('TestAnswer', () => {
    test('valid pair', () => {
        const nums = [2, 7, 11, 15];
        const target = 9;
        const expected = [0, 1]; // 2 + 7 = 9
        expect(twoSum(nums, target)).toEqual(expected);
    });

    test('negative numbers', () => {
        const nums = [-1, -2, -3, -4, -5];
        const target = -8;
        const expected = [2, 4]; // -3 + -5 = -8
        expect(twoSum(nums, target)).toEqual(expected);
    });

    test('zero sum', () => {
        const nums = [0, 4, 3, 0];
        const target = 0;
        const expected = [0, 3]; // 0 + 0 = 0
        expect(twoSum(nums, target)).toEqual(expected);
    });

    test('no solution', () => {
        const nums = [1, 2, 3, 4, 5];
        const target = 10;
        expect(() => twoSum(nums, target)).toThrow(Error);
    });

    test('same number twice', () => {
        const nums = [3, 3];
        const target = 6;
        const expected = [0, 1]; // 3 + 3 = 6
        expect(twoSum(nums, target)).toEqual(expected);
    });

    test('large numbers', () => {
        const nums = [2147483647, -2147483648, 0, 1];
        const target = 1;
        const expected = [2, 3]; // 0 + 1 = 1
        expect(twoSum(nums, target)).toEqual(expected);
    });
});
