/**
 * Stores a second-level string in a set of 8-bit conversion integers in a Unit8Array and returns
 *
 * @param {string} binaryStr - The binary string to be converted.
 * @returns {Uint8Array} - The resulting Uint8Array containing the binary data.
 */
function binaryStringToUint8Array(binaryStr: string): Uint8Array {
    // Calculate the number of bytes needed to represent the binary string
    const byteCount = Math.ceil(binaryStr.length / 8);
    const byteArray = new Uint8Array(byteCount);

    // Convert each 8-character segment of the binary string into a byte and store in byteArray
    for (let i = 0; i < byteCount; i++) {
        const byteSegment = binaryStr.substr(i * 8, 8);  // Extract 8 characters
        byteArray[i] = parseInt(byteSegment, 2);  // Convert binary segment to byte
    }

    return byteArray;
}
