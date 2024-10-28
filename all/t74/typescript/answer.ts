/**
 * Converts a decimal number to its binary representation in either 32-bit or 64-bit format.
 *
 * @param {number} decimalValue - The decimal number to convert.
 * @param {number} bitLength - The desired bit length for the binary representation (32 or 64).
 * @returns {string | null} The binary string representation of the decimal number if the bit length
 *                          is valid, otherwise `null`.
 * @throws {Error} Throws an error if the bit length is not 32 or 64.
 */
function convertDecimalToBinary(decimalValue: number, bitLength: number): string | null {
    if (bitLength === 32) {
        // Convert the decimal to a 32-bit binary representation
        const buffer = new ArrayBuffer(4);
        const floatView = new Float32Array(buffer);
        floatView[0] = decimalValue;
        const intView = new Int32Array(buffer);
        const binaryRepresentation = (intView[0] >>> 0).toString(2).padStart(32, '0');
        return binaryRepresentation;
    } else if (bitLength === 64) {
        // Convert the decimal to a 64-bit binary representation
        const buffer = new ArrayBuffer(8);
        const floatView = new Float64Array(buffer);
        floatView[0] = decimalValue;
        const intView = new BigInt64Array(buffer);
        const binaryRepresentation = (BigInt(intView[0]) >>> 0n).toString(2).padStart(64, '0');
        return binaryRepresentation;
    } else {
        throw new Error("Invalid bit length. Please specify either 32 or 64.");
    }
}
