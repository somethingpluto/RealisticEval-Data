describe('check_xor_sum', () => {
    test('should return true for correct XOR sums', () => {
        const combination = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ];
        expect(check_xor_sum(combination)).toBe(true);
    });

    test('should return false for incorrect XOR sums', () => {
        const combination = [
            [0, 1, 0],
            [1, 0, 1],
            [1, 1, 0] // Incorrect XOR sum for the third column
        ];
        expect(check_xor_sum(combination)).toBe(false);
    });
});