import { printMemoryBits } from './yourModule'; // Adjust the import according to where your function is defined
import { jest } from '@jest/globals';

describe('printMemoryBits', () => {
    let consoleSpy: jest.SpyInstance;

    beforeEach(() => {
        // Mock console.log
        consoleSpy = jest.spyOn(console, 'log').mockImplementation(() => {});
    });

    afterEach(() => {
        // Restore the original console.log
        consoleSpy.mockRestore();
    });

    test('single byte', () => {
        const memorySection = new Uint8Array([0b10101010]);
        printMemoryBits(memorySection);
        const output = consoleSpy.mock.calls.map(call => call.join(' ')).join('\n').trim();
        const expectedOutput = "0 1 0 1 0 1 0 1 0";
        expect(output).toBe(expectedOutput);
    });

    test('multiple bytes', () => {
        const memorySection = new Uint8Array([0b11001100, 0b11110000]);
        printMemoryBits(memorySection);
        const output = consoleSpy.mock.calls.map(call => call.join(' ')).join('\n').trim();
        const expectedOutput = "0 1 1 0 0 1 1 0 0\n1 1 1 1 0 0 0 0";
        expect(output).toBe(expectedOutput);
    });

    test('all zeros', () => {
        const memorySection = new Uint8Array([0b00000000]);
        printMemoryBits(memorySection);
        const output = consoleSpy.mock.calls.map(call => call.join(' ')).join('\n').trim();
        const expectedOutput = "0 0 0 0 0 0 0 0";
        expect(output).toBe(expectedOutput);
    });

    test('all ones', () => {
        const memorySection = new Uint8Array([0b11111111]);
        printMemoryBits(memorySection);
        const output = consoleSpy.mock.calls.map(call => call.join(' ')).join('\n').trim();
        const expectedOutput = "0 1 1 1 1 1 1 1 1";
        expect(output).toBe(expectedOutput);
    });

    test('mixed bytes', () => {
        const memorySection = new Uint8Array([0b01010101, 0b10000001]);
        printMemoryBits(memorySection);
        const output = consoleSpy.mock.calls.map(call => call.join(' ')).join('\n').trim();
        const expectedOutput = "0 0 1 0 1 0 1 0 1\n1 1 0 0 0 0 0 0 1";
        expect(output).toBe(expectedOutput);
    });
});