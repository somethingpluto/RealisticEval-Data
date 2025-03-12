/**
 * Find the powers of 2 and 3 that multiply to produce the given number.
 *
 * @param {number} num - A positive integer greater than zero.
 * @returns {Array|null} An array [n, m] where n is the power of 2 and m is the power of 3.
 *                       Returns null if the number is zero or if the number has prime factors other than 2 and 3.
 */
function findPowers(num) {
    if (num <= 0) {
        return null;
    }

    let powerOf2 = 0;
    let powerOf3 = 0;

    // Divide by 2 until num is no longer divisible by 2
    while (num % 2 === 0) {
        num /= 2;
        powerOf2++;
    }

    // Divide by 3 until num is no longer divisible by 3
    while (num % 3 === 0) {
        num /= 3;
        powerOf3++;
    }

    // If num is not 1, it means there are other prime factors
    if (num !== 1) {
        return null;
    }

    return [powerOf2, powerOf3];
}
describe('TestFindPowers', () => {
    describe('Valid Cases', () => {
        it('should handle valid numbers with only 2\'s and 3\'s as prime factors', () => {
            expect(findPowers(18)).toEqual([1, 2]);  // 18 = 2^1 * 3^2
            expect(findPowers(8)).toEqual([3, 0]);   // 8 = 2^3 * 3^0
            expect(findPowers(27)).toEqual([0, 3]);  // 27 = 2^0 * 3^3
            expect(findPowers(12)).toEqual([2, 1]);  // 12 = 2^2 * 3^1
            expect(findPowers(1)).toEqual([0, 0]);   // 1 = 2^0 * 3^0
        });
    });

    describe('Invalid Cases', () => {
        it('should handle numbers with prime factors other than 2 and 3', () => {
            expect(findPowers(7)).toBeNull();    // 7 is a prime factor
            expect(findPowers(14)).toBeNull();   // 14 = 2^1 * 7^1 (contains 7)
            expect(findPowers(10)).toBeNull();   // 10 = 2^1 * 5^1 (contains 5)
        });
    });

    describe('Large Numbers', () => {
        it('should handle large numbers that have only 2 and 3 as prime factors', () => {
            expect(findPowers(864)).toEqual([5, 3]);  // 864 = 2^5 * 3^3
            expect(findPowers(729)).toEqual([0, 6]);  // 729 = 2^0 * 3^6
        });
    });

    describe('Edge Cases', () => {
        it('should handle edge cases for minimal inputs', () => {
            expect(findPowers(2)).toEqual([1, 0]);   // 2 = 2^1 * 3^0
            expect(findPowers(3)).toEqual([0, 1]);   // 3 = 2^0 * 3^1
        });
    });
});
