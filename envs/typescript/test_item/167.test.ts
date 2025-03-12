// Start of the code context
import { assert } from 'assert';

/**
 * Determines whether a given string (assumed to end with ".bit") is a valid 3-digit integer.
 * Removes the ".bit" suffix, checks if the remaining part is a number and verifies if it falls within the range of 0 to 999.
 *
 * @param {string} bitName - The string to validate.
 * @returns {boolean} True if the remaining part after removing ".bit" is a valid 3-digit integer, otherwise false.
 */
function assert999(bitName: string): boolean {
    const numberPart = bitName.replace('.bit', '');
    const isValidNumber = !isNaN(parseInt(numberPart, 10));
    const isInRange = isValidNumber && parseInt(numberPart, 10) >= 0 && parseInt(numberPart, 10) <= 999;
    return isInRange;
}

// Unit tests
describe('assert999', () => {
    it('should return true for valid 3-digit integers', () => {
        assert.strictEqual(assert999('123.bit'), true);
        assert.strictEqual(assert999('001.bit'), true);
        assert.strictEqual(assert999('999.bit'), true);
    });

    it('should return false for invalid 3-digit integers', () => {
        assert.strictEqual(assert999('1000.bit'), false);
        assert.strictEqual(assert999('99.bit'), false);
        assert.strictEqual(assert999('100.bit'), false);
    });

    it('should return false for non-integer values', () => {
        assert.strictEqual(assert999('abc.bit'), false);
        assert.strictEqual(assert999('12.34.bit'), false);
    });

    it('should return false for strings without .bit suffix', () => {
        assert.strictEqual(assert999('123'), false);
    });
});
// End of the code context
describe('assert999', () => {
    /**
     * Test case for a valid 3-digit number with the ".bit" suffix.
     * Expected to return true.
     */
    test('should return true for a valid 3-digit number with ".bit" suffix', () => {
        const input = "123.bit";
        const result = assert999(input);
        expect(result).toBe(true);
    });

    /**
     * Test case for a string without the ".bit" suffix.
     * Expected to return false.
     */
    test('should return true for a valid 2-digit number with ".bit" suffix', () => {
        const input = "12.bit";
        const result = assert999(input);
        expect(result).toBe(true);
    });

    /**
     * Test case for a string containing non-numeric characters after removing ".bit".
     * Expected to return false.
     */
    test('should return false for a string with non-numeric characters after removing ".bit"', () => {
        const input = "12a.bit";
        const result = assert999(input);
        expect(result).toBe(false);
    });

    /**
     * Test case for the lower boundary value "0.bit".
     * Expected to return true.
     */
    test('should return true for the lower boundary value "0.bit"', () => {
        const input = "0.bit";
        const result = assert999(input);
        expect(result).toBe(true);
    });

    /**
     * Test case for the upper boundary value "999.bit".
     * Expected to return true.
     */
    test('should return true for the upper boundary value "999.bit"', () => {
        const input = "999.bit";
        const result = assert999(input);
        expect(result).toBe(true);
    });
});


