describe('binaryStringToUint8Array', () => {
    test('should convert a full byte binary string', () => {
        const binaryStr = '11001010';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([202]));
    });

    test('should convert multiple full byte binary strings', () => {
        const binaryStr = '1100101011110000';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([202, 240]));
    });

    test('should convert a binary string with fewer than 8 bits', () => {
        const binaryStr = '110';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([6]));
    });

    test('should convert a binary string with non-multiples of 8 bits', () => {
        const binaryStr = '110010101';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([202, 1]));
    });

    test('should handle an empty binary string', () => {
        const binaryStr = '';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([]));
    });
});