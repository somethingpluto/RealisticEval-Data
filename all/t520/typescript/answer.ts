function computeOutputIndex(idx1: number, idx2: number): number {
    // Perform bitwise XOR between the two indices
    let result = idx1 ^ idx2;

    // Convert result to little-endian byte representation
    const resultBytes: number[] = [];
    while (result > 0) {
        resultBytes.push(result & 0xFF);  // Push the least significant byte
        result >>= 8;  // Shift right by 8 bits (1 byte)
    }

    // If no bytes were added (result was 0), we need at least one byte
    if (resultBytes.length === 0) {
        resultBytes.push(0);
    }

    // Convert the bytes back to an integer, interpreting them as little-endian
    let resultInt = 0;
    for (let i = 0; i < resultBytes.length; i++) {
        resultInt |= resultBytes[i] << (8 * i);
    }

    return resultInt;
}
