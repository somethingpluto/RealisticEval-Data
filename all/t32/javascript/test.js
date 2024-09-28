const { CRC64 } = require('./path_to_crc64_class'); // Adjust the import path as necessary

describe('CRC64', () => {

    test('initialization of CRC64 table', () => {
        CRC64.crc64_init_table();
        expect(CRC64.crc64_tab.length).toBe(256);
        expect(CRC64.crc64_tab.every(x => typeof x === 'bigint')).toBe(true);
    });

    test('crc64_update with known values', () => {
        CRC64.crc64_init_table();
        const initial_crc = 0xFFFFFFFFFFFFFFFFn;
        const byte = 0x01;
        const updated_crc = CRC64.crc64_update(initial_crc, byte);
        const expected_crc = (CRC64.crc64_tab[0xFE] ^ (initial_crc >> 8n)) & 0xFFFFFFFFFFFFFFFFn;
        expect(updated_crc).toBe(expected_crc);
    });

    test('compute with positive integer', () => {
        const result = CRC64.compute(1234567890n);
        const expected_result = 0xB0F9361BAEB8A24En;
        expect(result).toBe(expected_result);
    });

    test('compute with negative integer', () => {
        const result = CRC64.compute(-1234567890n);
        const expected_result = 0x865B548A1C95DB76n;
        expect(result).toBe(expected_result);
    });

    test('compute with zero', () => {
        const result = CRC64.compute(0n);
        const expected_result = 0xB90956C775A41001n;
        expect(result).toBe(expected_result);
    });
});