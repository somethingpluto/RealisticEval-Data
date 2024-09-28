const { printMemoryBits } = require('./yourModule'); // Adjust the path to the location of your printMemoryBits function

describe('printMemoryBits', () => {
    let originalStdoutWrite;
    let capturedOutput;

    // Capture the output before each test
    beforeEach(() => {
        originalStdoutWrite = process.stdout.write;
        capturedOutput = '';
        process.stdout.write = (chunk) => {
            capturedOutput += chunk;
        };
    });

    // Restore the original stdout after each test
    afterEach(() => {
        process.stdout.write = originalStdoutWrite;
    });

    test('single byte', () => {
        const memorySection = new Uint8Array([0b10101010]);
        printMemoryBits(memorySection);
        const expectedOutput = "Byte 0: 1 0 1 0 1 0 1 0 \n";
        expect(capturedOutput).toBe(expectedOutput);
    });

    test('multiple bytes', () => {
        const memorySection = new Uint8Array([0b11001100, 0b11110000]);
        printMemoryBits(memorySection);
        const expectedOutput = "Byte 0: 1 1 0 0 1 1 0 0 \nByte 1: 1 1 1 1 0 0 0 0 \n";
        expect(capturedOutput).toBe(expectedOutput);
    });

    test('all zeros', () => {
        const memorySection = new Uint8Array([0b00000000]);
        printMemoryBits(memorySection);
        const expectedOutput = "Byte 0: 0 0 0 0 0 0 0 0 \n";
        expect(capturedOutput).toBe(expectedOutput);
    });

    test('all ones', () => {
        const memorySection = new Uint8Array([0b11111111]);
        printMemoryBits(memorySection);
        const expectedOutput = "Byte 0: 1 1 1 1 1 1 1 1 \n";
        expect(capturedOutput).toBe(expectedOutput);
    });

    test('mixed bytes', () => {
        const memorySection = new Uint8Array([0b01010101, 0b10000001]);
        printMemoryBits(memorySection);
        const expectedOutput = "Byte 0: 0 1 0 1 0 1 0 1 \nByte 1: 1 0 0 0 0 0 0 1 \n";
        expect(capturedOutput).toBe(expectedOutput);
    });
});