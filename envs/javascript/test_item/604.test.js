/**
 * Tail-recursive function to calculate x raised to the power y.
 *
 * This function uses tail recursion to compute x^y.
 *
 * @param {number} x The base, a non-negative integer.
 * @param {number} y The exponent, a non-negative integer.
 * @param {number} acc The accumulator to hold the intermediate result.
 *
 * @return {number} The result of x raised to the power of y.
 */
function powerTail(x, y, acc = 1) {
    // Base case: if y is 0, return the accumulator
    if (y === 0) {
        return acc;
    }
    // Recursive case: multiply the accumulator by x and decrement y
    return powerTail(x, y - 1, acc * x);
}
describe('Power function test cases', () => {
    describe('Base cases', () => {
        // Test 0^0, should return 1 (by convention)
        test('0^0 should return 1', () => {
            expect(powerTail(0, 0)).toBe(1);
        });

        // Test x^0 for any x, should return 1
        test('5^0 should return 1', () => {
            expect(powerTail(5, 0)).toBe(1);
        });
        
        test('12345^0 should return 1', () => {
            expect(powerTail(12345, 0)).toBe(1);
        });
    });

    describe('Power of one', () => {
        // Test 1^y for any y, should return 1
        test('1^5 should return 1', () => {
            expect(powerTail(1, 5)).toBe(1);
        });

        test('1^123 should return 1', () => {
            expect(powerTail(1, 123)).toBe(1);
        });
    });

    describe('Power of zero', () => {
        // Test 0^y for any y > 0, should return 0
        test('0^5 should return 0', () => {
            expect(powerTail(0, 5)).toBe(0);
        });

        test('0^100 should return 0', () => {
            expect(powerTail(0, 100)).toBe(0);
        });
    });

    describe('Positive powers', () => {
        // Test some positive powers
        test('2^3 should return 8', () => {
            expect(powerTail(2, 3)).toBe(8); // 2^3 = 8
        });

        test('3^4 should return 81', () => {
            expect(powerTail(3, 4)).toBe(81); // 3^4 = 81
        });

        test('5^2 should return 25', () => {
            expect(powerTail(5, 2)).toBe(25); // 5^2 = 25
        });
    });
});
