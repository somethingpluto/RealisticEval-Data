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


    test('should handle an empty binary string', () => {
        const binaryStr = '';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([]));
    });

    test('should correctly convert binary string with leading zeros', () => {
        const binaryStr = '00101101';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([45]));
    });
    test('should handle binary string with end padding of zeros', () => {
    const binaryStr = '11001010000'; // should be treated as '11001010 00000000'
    // @ts-ignore
    const result = binaryStringToUint8Array(binaryStr);
    expect(result).toEqual(new Uint8Array([202, 0]));
});
});
