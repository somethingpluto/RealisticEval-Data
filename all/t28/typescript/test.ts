describe('TestPrintMemoryBits', () => {
    // Helper function to capture console output
    const captureOutput = (fn: () => void): string => {
        const originalConsoleLog = console.log;
        let capturedOutput = '';

        console.log = (message?: any) => {
            capturedOutput += message + '\n';
        };

        fn();

        console.log = originalConsoleLog;
        return capturedOutput.trim();
    };

    test('test_single_byte', () => {
        const memorySection = new Uint8Array([0b10101010]);
        const output = captureOutput(() => printMemoryBits(memorySection));
        expect(output).toBe("10101010");
    });

    test('test_multiple_bytes', () => {
        const memorySection = new Uint8Array([0b11001100, 0b11110000]);
        const output = captureOutput(() => printMemoryBits(memorySection));
        expect(output).toBe("11001100\n11110000");
    });

    test('test_all_zeros', () => {
        const memorySection = new Uint8Array([0b00000000]);
        const output = captureOutput(() => printMemoryBits(memorySection));
        expect(output).toBe("00000000");
    });

    test('test_all_ones', () => {
        const memorySection = new Uint8Array([0b11111111]);
        const output = captureOutput(() => printMemoryBits(memorySection));
        expect(output).toBe("11111111");
    });
});