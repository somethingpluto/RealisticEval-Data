describe('printMemoryBits', () => {
    let originalConsoleLog;

    beforeEach(() => {
        // Capture the console.log output
        originalConsoleLog = console.log;
        console.log = jest.fn(); // Mock console.log
    });

    afterEach(() => {
        // Restore the original console.log
        console.log = originalConsoleLog;
    });

    test('prints a single byte', () => {
        const memorySection = new Uint8Array([0b10101010]);
        printMemoryBits(memorySection);
        expect(console.log).toHaveBeenCalledWith('10101010');
    });

    test('prints multiple bytes', () => {
        const memorySection = new Uint8Array([0b11001100, 0b11110000]);
        printMemoryBits(memorySection);
        expect(console.log).toHaveBeenCalledWith('11001100');
        expect(console.log).toHaveBeenCalledWith('11110000');
    });

    test('prints all zeros', () => {
        const memorySection = new Uint8Array([0b00000000]);
        printMemoryBits(memorySection);
        expect(console.log).toHaveBeenCalledWith('00000000');
    });

    test('prints all ones', () => {
        const memorySection = new Uint8Array([0b11111111]);
        printMemoryBits(memorySection);
        expect(console.log).toHaveBeenCalledWith('11111111');
    });
});
