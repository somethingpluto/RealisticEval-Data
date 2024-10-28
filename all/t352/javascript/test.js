describe('hexStringToByteArray', () => {
    test('normal hex string', () => {
        const hexStr = "1a3f";
        const expected = new Uint8Array([0x1A, 0x3F]);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
        // Assertion message is not included in Jest by default
    });

    test('odd length hex string', () => {
        const hexStr = "123";
        const expected = new Uint8Array([0x01, 0x23]);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
    });

    test('empty string', () => {
        const hexStr = "";
        const expected = new Uint8Array([]);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
    });

    test('hex string with uppercase', () => {
        const hexStr = "1A3F";
        const expected = new Uint8Array([0x1A, 0x3F]);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
    });
});