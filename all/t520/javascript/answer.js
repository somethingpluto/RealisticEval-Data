function computeOutputIndex(idx1, idx2) {
    /**
     * Computes the output index from two given indices in the MultiVector's representation
     * of the G_n orthonormal basis.
     *
     * This function interprets the integers as little-endian bitstrings, takes their XOR,
     * and interprets the result as an integer in little-endian.
     *
     * @param {number} idx1 - Input index 1.
     * @param {number} idx2 - Input index 2.
     *
     * @returns {number} The computed output index.
     */

    // Perform bitwise XOR between the two indices
    let result = idx1 ^ idx2;

    // Convert result to little-endian byte representation
    let resultBytes = new Uint8Array((result.bitLength() + 7) / 8);
    for (let i = 0; i < resultBytes.length; i++) {
        resultBytes[i] = result & 0xff;
        result >>= 8;
    }

    // Convert little-endian bytes back to an integer
    let resultInt = 0;
    for (let byte of resultBytes) {
        resultInt = (resultInt << 8) | byte;
    }

    return resultInt;
}