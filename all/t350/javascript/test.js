describe('TestAnswer', () => {
    test('empty byte array', () => {
        const inputData = new Uint8Array(); // Empty byte array
        expect(byteArrayToHexString(inputData)).toBe(""); // Jest equivalent of assertEqual
    });

    test('single byte', () => {
        const inputData = new Uint8Array([0x0F]); // 15 in decimal
        const result = byteArrayToHexString(inputData);
        expect(["0F", "0f"]).toContain(result); // Jest equivalent of assertTrue with array inclusion
    });

    test('multiple bytes', () => {
        const inputData = new Uint8Array([0x01, 0x0A, 0xFF]);
        const result = byteArrayToHexString(inputData);
        expect(["010aff", "010AFF"]).toContain(result); // Same as above
    });

    test('zero bytes', () => {
        const inputData = new Uint8Array([0x00, 0x00, 0x00]);
        expect(byteArrayToHexString(inputData)).toBe("000000"); // Jest equivalent of assertEqual
    });

    test('negative bytes', () => {
        const inputData = new Uint8Array([0x80, 0xFF]); // 128 and 255 in signed byte representation
        const result = byteArrayToHexString(inputData);
        expect(["80FF", "80ff"]).toContain(result); // Same as above
    });
});