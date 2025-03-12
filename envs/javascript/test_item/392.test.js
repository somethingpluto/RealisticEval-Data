/**
 * Generates the next sequence in the 'look-and-say' sequence by reading off the digits of the given number,
 * grouping by consecutive digits.
 *
 * @param {string} number - The current sequence as a string.
 * @returns {string} - The next sequence in the 'look-and-say' series.
 */
function lookAndSay(number) {
    let result = '';
    let count = 1;

    for (let i = 0; i < number.length; i++) {
        if (i + 1 < number.length && number[i] === number[i + 1]) {
            count++;
        } else {
            result += count + number[i];
            count = 1;
        }
    }

    return result;
}
describe('TestLookAndSay', () => {
    test('test_single_digit', () => {
        // Test with a single digit to see if it replicates correctly
        expect(lookAndSay('1')).toBe('11');
    });

    test('test_repetitive_digits', () => {
        // Test a sequence of the same digits
        expect(lookAndSay('111')).toBe('31');
    });

    test('test_mixed_digits', () => {
        // Test a sequence with different digits
        expect(lookAndSay('1211')).toBe('111221');
    });

    test('test_complex_sequence', () => {
        // Test a more complex sequence
        expect(lookAndSay('312211')).toBe('13112221');
    });
});
