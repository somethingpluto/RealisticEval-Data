function printMemoryBits(memorySection: Uint8Array): void {
    /**
     * Prints the status of each bit (0 or 1) in the given section of memory.
     *
     * @param memorySection - A Uint8Array representing the section of memory to be read.
     */
    for (let byte of memorySection) {
        console.log(Array.from({ length: 8 }, (_, i) => (byte >> (7 - i)) & 1).join(''));
    }
}