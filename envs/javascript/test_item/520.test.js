/**
 * Computes the output index from two given indices in the MultiVector's representation
 * of the G_n orthonormal basis.
 *
 * This function interprets the integers as little-endian bitstrings, takes their XOR,
 * and interprets the result as an integer in little-endian.
 *
 * @param {number} idx1 - Input index 1.
 * @param {number} idx2 - Input index 2.
 * @returns {number} The computed output index.
 */
function computeOutputIndex(idx1, idx2) {
    // Convert the indices to little-endian bitstrings
    let bitstring1 = idx1.toString(2).split('').reverse().join('');
    let bitstring2 = idx2.toString(2).split('').reverse().join('');

    // Ensure both bitstrings are of the same length by padding with zeros
    const maxLength = Math.max(bitstring1.length, bitstring2.length);
    bitstring1 = bitstring1.padEnd(maxLength, '0');
    bitstring2 = bitstring2.padEnd(maxLength, '0');

    // Perform XOR operation on the bitstrings
    let resultBitstring = '';
    for (let i = 0; i < maxLength; i++) {
        resultBitstring += (bitstring1[i] === bitstring2[i]) ? '0' : '1';
    }

    // Convert the result bitstring back to an integer in little-endian
    const outputIndex = parseInt(resultBitstring.split('').reverse().join(''), 2);

    return outputIndex;
}
describe('TestComputeOutputIndex', () => {
    it('test_standard_case', () => {
        // Test with two standard positive integers
        const idx_1 = 3;  // binary: 11
        const idx_2 = 5;  // binary: 101
        const expected = 6;  // 3 XOR 5 = 6
        const result = computeOutputIndex(idx_1, idx_2);
        expect(result).toEqual(expected);
    });

    it('test_identical_indices', () => {
        // Test with identical indices (should return 0)
        const idx_1 = 7;  // binary: 111
        const idx_2 = 7;  // binary: 111
        const expected = 0;  // 7 XOR 7 = 0
        const result = computeOutputIndex(idx_1, idx_2);
        expect(result).toEqual(expected);
    });

    it('test_zero_index', () => {
        // Test with one index as zero
        const idx_1 = 0;  // binary: 0
        const idx_2 = 5;  // binary: 101
        const expected = 5;  // 0 XOR 5 = 5
        const result = computeOutputIndex(idx_1, idx_2);
        expect(result).toEqual(expected);
    });

    it('test_large_numbers', () => {
        // Test with large integer values
        const idx_1 = 1024;  // binary: 10000000000
        const idx_2 = 2048;  // binary: 100000000000
        const expected = 3072;  // 1024 XOR 2048 = 3072
        const result = computeOutputIndex(idx_1, idx_2);
        expect(result).toEqual(expected);
    });
});
