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