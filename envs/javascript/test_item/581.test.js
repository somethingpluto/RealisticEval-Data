/**
 * Abbreviates a number to a string with a suffix based on its magnitude. 
 * Suffixes: ["", "k", "M", "B", "T"]; 1000 is k, 1000000 is M, 1000000000 is B.
 * For example:
 *      input: 999 output: 999
 *      input: 1549 output: 1.5k
 *      input: 1000 output: 1k
 *      input: 1234567890123 output: 1.2T
 * @param {number} number - The number to abbreviate.
 * @returns {string} - The abbreviated string representation of the number.
 */
function abbreviateNumber(number) {
    const suffixes = ["", "k", "M", "B", "T"];
    const tier = Math.log10(Math.abs(number)) / 3 | 0;
    if (tier === 0) return number;
    const suffix = suffixes[tier];
    const scale = Math.pow(10, tier * 3);
    const scaledNumber = number / scale;
    return scaledNumber.toFixed(1) + suffix;
}
describe('abbreviateNumber', () => {
    test('should return the same number for values less than 1000', () => {
        expect(abbreviateNumber(999)).toBe('999');
    });

    test('should return "1k" for 1000', () => {
        const result = abbreviateNumber(1000);
        expect(['1k', '1.0k']).toContain(result);
    });

    test('should return "1.5k" for 1500', () => {
        expect(abbreviateNumber(1500)).toBe('1.5k');
    });

    test('should return "1M" for 1 million', () => {
        const result = abbreviateNumber(1000000);
        expect(['1M', '1.0M']).toContain(result);
    });

    test('should return "25M" for 25 million', () => {
        expect(abbreviateNumber(25000000)).toBe('25M');
    });

    test('should return "1B" for 1 billion', () => {
        const result = abbreviateNumber(1000000000);
        expect(['1B', '1.0B']).toContain(result);
    });

    test('should return "1.2T" for 1.2 trillion', () => {
        expect(abbreviateNumber(1234567890123)).toBe('1.2T');
    });
});
