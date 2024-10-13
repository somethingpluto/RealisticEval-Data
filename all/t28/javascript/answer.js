function printMemoryBits(memorySection) {
    /**
     * Prints the status of each bit (0 or 1) in the given section of memory.
     *
     * @param {Uint8Array} memorySection - An Uint8Array representing the section of memory to be read.
     */
    for (let byte of memorySection) {
        let bits = '';
        for (let i = 7; i >= 0; i--) {
            bits += (byte >> i) & 1;
        }
        console.log(bits);
    }
}