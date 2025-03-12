/**
 * Finds the largest integer between a given number n and half of it that is divisible by 10 or 5.
 * 
 * @param {number} n - The upper bound of the range.
 * @returns {(number | null)} - The largest integer between n and half of n that is divisible by 5, or
 *                              null if no such number exists.
 */
function findLargestDivisible(n) {
    // Ensure n is an integer
    if (!Number.isInteger(n) || n <= 0) {
        return null;
    }

    // Calculate half of n
    const halfN = Math.floor(n / 2);

    // Iterate from n down to halfN
    for (let i = n; i >= halfN; i--) {
        if (i % 5 === 0) {
            return i;
        }
    }

    // If no number is found, return null
    return null;
}
describe('findLargestDivisible', () => {
    test('test typical case', () => {
        /** Test with a typical input where the largest divisible number should be found. */
        expect(findLargestDivisible(50)).toBe(50);
        expect(findLargestDivisible(47)).toBe(45);
    });

    test('test no divisible number found', () => {
        /** Test a case where no divisible number is found within the range. */
        expect(findLargestDivisible(4)).toBeNull();
    });

    test('test exact half divisible', () => {
        /** Test when the half of n is exactly divisible by 5. */
        expect(findLargestDivisible(10)).toBe(10);
    });

    test('test large number', () => {
        /** Test with a large number to ensure performance and correctness. */
        expect(findLargestDivisible(1000)).toBe(1000);
    });

    test('test lower bound', () => {
        /** Test the function with the lowest bound that should find a divisible number. */
        expect(findLargestDivisible(5)).toBe(5);
    });
});
