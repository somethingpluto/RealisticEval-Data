function bitsToBytes(bits: number[]): Uint8Array {
    // Calculate the number of full bytes that can be formed
    const numFullBytes = Math.floor(bits.length / 8);

    // Create a new Uint8Array with the calculated number of full bytes
    const bytes = new Uint8Array(numFullBytes);

    for (let i = 0; i < numFullBytes; i++) {
        let byteValue = 0;

        // Compose 8 bits into one byte
        for (let j = 0; j < 8; j++) {
            byteValue = (byteValue << 1) | bits[i * 8 + j];
        }

        // Store the composed byte in the array
        bytes[i] = byteValue;
    }

    return bytes;
}