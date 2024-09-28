function printMemoryBits(memorySection) {
    /**
     * Prints the status of each bit (0 or 1) in the given section of memory.
     * Print format: e.g., Byte 0: 1 1 0 0 1 1 0 0 \nByte 1: 1 1 1 1 0 0 0 0
     *
     * @param memorySection: A Uint8Array representing the section of memory to be read.
     */
    memorySection.forEach((byte, byteIndex) => {
        process.stdout.write(`Byte ${byteIndex}: `);
        for (let bitIndex = 0; bitIndex < 8; bitIndex++) {
            // Shift the bit to the right and check the least significant bit
            let bitStatus = (byte >> (7 - bitIndex)) & 1;
            process.stdout.write(`${bitStatus} `);
        }
        console.log(); // Newline after each byte
    });
}

// Example usage:
// const memorySection = new Uint8Array([204, 240]);
// printMemoryBits(memorySection);