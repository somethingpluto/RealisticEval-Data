import * as math from 'mathjs';

/**
 * Checks the XOR sums of specific columns in a given combination array.
 *
 * @param combination - A 2D array where each column corresponds to a specific value.
 * @returns true if the XOR sums of the specified columns match the required values; otherwise, false.
 */
function checkXorSum(combination: number[][]): boolean {
    // Ensure that combination is an array of integers
    const intCombination = combination.map(row => row.map(num => Math.floor(num)));

    // Calculate XOR sums for specified columns
    const xorSum036 = intCombination.map(row => row[0] ^ row[3] ^ row[6]);
    const xorSum147 = intCombination.map(row => row[1] ^ row[4] ^ row[7]);
    const xorSum25 = intCombination.map(row => row[2] ^ row[5]);

    // Check if the XOR sums match the expected values
    return xorSum036.every(val => val === 0x6b) &&
           xorSum147.every(val => val === 0x76) &&
           xorSum25.every(val => val === 0x12);
}