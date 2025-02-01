/**
 * Increments the entered number.
 * If the number is non-positive (<= 0), returns the original value.
 * If the number is positive, returns the value plus 1.
 *
 * @param {number} num - The number to increment.
 * @returns {number} - The incremented value or the original number.
 */
function incrementNumber(num) {
    if (num > 0) {
        return num + 1;
    } else {
        return num;
    }
}
describe('incrementNumber', () => {
    test('should return 6 when input is 5', () => {
        expect(incrementNumber(5)).toBe(6);
    });

    test('should return 0 when input is 0', () => {
        expect(incrementNumber(0)).toBe(0);
    });

    test('should return -3 when input is -3', () => {
        expect(incrementNumber(-3)).toBe(-3);
    });

    test('should return 1 when input is 0.5', () => {
        expect(incrementNumber(0.5)).toBe(1.5);
    });

    test('should return 1 when input is 1', () => {
        expect(incrementNumber(1)).toBe(2);
    });

    test('should return -1 when input is -1', () => {
        expect(incrementNumber(-1)).toBe(-1);
    });
});
