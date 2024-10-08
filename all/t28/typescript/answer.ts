function printMemoryBits(memorySection: Uint8Array) {
    /**
     * Prints the status of each bit (0 or 1) in the given section of memory.
     * Print format example: Byte 0: 1 1 0 0 1 1 0 0 \nByte 1: 1 1 1 1 0 0 0 0
     *
     * @param memorySection - A Uint8Array representing the section of memory to be read.
     */
    for (let byteIndex = 0; byteIndex < memorySection.length; byteIndex++) {
        const byte = memorySection[byteIndex];
        process.stdout.write(`${byteIndex} `);
        for (let bitIndex = 0; bitIndex < 8; bitIndex++) {
            // Shift the bit to the right and check the least significant bit
            const bitStatus = (byte >> (7 - bitIndex)) & 1;
            process.stdout.write(`${bitStatus} `);
        }
        console.log();  // Newline after each byte
    }
}