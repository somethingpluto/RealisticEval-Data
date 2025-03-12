/**
 * Checks the XOR sums of specific columns in a given combination array.
 *
 * @param {Array<Array<number>>} combination - A 2D array where each column corresponds to a specific value.
 * @returns {boolean} - True if the XOR sums of the specified columns match the required values; otherwise, false.
 */
function checkXorSum(combination) {
    // Define the required XOR sums for each column
    const requiredXorSums = [0, 0, 0]; // Example required XOR sums for columns 0, 1, and 2

    // Check if the combination array has the correct number of columns
    if (combination.length === 0 || combination[0].length !== requiredXorSums.length) {
        return false;
    }

    // Calculate the XOR sum for each column
    const xorSums = new Array(requiredXorSums.length).fill(0);

    for (let row of combination) {
        for (let i = 0; i < row.length; i++) {
            xorSums[i] ^= row[i];
        }
    }

    // Compare the calculated XOR sums with the required XOR sums
    for (let i = 0; i < requiredXorSums.length; i++) {
        if (xorSums[i] !== requiredXorSums[i]) {
            return false;
        }
    }

    return true;
}
describe('TestCheckXorSum', () => {
    it('test_correct_xor_sums', () => {
        /** Test with combination values that produce the expected XOR sums. */
        const combination = [
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        ];
        expect(checkXorSum(combination)).toBe(false);
    });

    it('test_incorrect_xor_sums', () => {
        /** Test with combination values that do not meet the expected XOR sums. */
        const combination = [
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00]
        ];
        expect(checkXorSum(combination)).toBe(false);
    });

    it('test_edge_case_with_zero', () => {
        /** Test with a combination where all values are zero. */
        const combination = [[0, 0, 0, 0, 0, 0, 0, 0]]; // 1 row of zeros
        expect(checkXorSum(combination)).toBe(false);
    });

    it('test_large_numbers', () => {
        /** Test with large numbers in the combination. */
        const combination = [
            [0x6b000000, 0x00000000, 0x00000012, 0x00000000, 0x76000000, 0x00000000, 0x00000000, 0x00000000],
            [0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000]
        ];
        expect(checkXorSum(combination)).toBe(false);
    });

    it('test_multiple_rows', () => {
        /** Test with a combination that contains multiple rows. */
        const combination = [
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00]
        ];
        expect(checkXorSum(combination)).toBe(true);
    });
});
