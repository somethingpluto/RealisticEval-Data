import { CRC64 } from './CRC64'; // Adjust the import according to your file structure

describe('CRC64', () => {
    test('should initialize CRC64 table correctly', () => {
        // Ensure the CRC64 table is initialized correctly
        CRC64['crc64InitTable']();
        expect(CRC64['crc64Tab'].length).toBe(256);
        expect(CRC64['crc64Tab'].every((x: bigint) => typeof x === 'bigint')).toBe(true);
    });

    test('should update CRC64 correctly with known values', () => {
        // Test crc64_update with known values
        CRC64['crc64InitTable']();
        const initialCrc = 0xFFFFFFFFFFFFFFFFn;
        const byte = 0x01;
        const updatedCrc = CRC64['crc64Update'](initialCrc, byte);
        const expectedCrc = (CRC64['crc64Tab'][0xFE] ^ (initialCrc >> 8n)) & 0xFFFFFFFFFFFFFFFFn;
        expect(updatedCrc).toBe(expectedCrc);
    });

    test('should compute CRC64 for a positive integer', () => {
        // Test compute method with a positive integer
        const result = CRC64.compute(1234567890);
        const expectedResult = 0xB0F9361BAEB8A24En;
        expect(result).toBe(expectedResult);
    });

    test('should compute CRC64 for a negative integer', () => {
        // Test compute method with a negative integer
        const result = CRC64.compute(-1234567890);
        const expectedResult = 0x865B548A1C95DB76n;
        expect(result).toBe(expectedResult);
    });

    test('should compute CRC64 for zero', () => {
        // Test compute method with zero
        const result = CRC64.compute(0);
        const expectedResult = 0xB90956C775A41001n; // Example CRC64 result for zero
        expect(result).toBe(expectedResult);
    });
});