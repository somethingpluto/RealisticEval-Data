function bitsToBytes(bits) {
    const numFullBytes = Math.floor(bits.length / 8);

    // Create a Uint8Array to store the byte values
    const byteArray = new Uint8Array(numFullBytes);

    // Process each group of 8 bits
    for (let i = 0; i < numFullBytes; i++) {
        // Slice the bits array to get 8 bits
        const byteBits = bits.slice(i * 8, (i + 1) * 8);
        // Convert the list of bits to a string of bits
        const byteStr = byteBits.join('');
        // Convert the string of bits to an integer and then to a byte
        const byte = parseInt(byteStr, 2);
        // Set the byte in the Uint8Array
        byteArray[i] = byte;
    }

    return byteArray;
}