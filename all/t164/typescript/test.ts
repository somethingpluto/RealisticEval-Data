describe('uint8ArrayToBase64', () => {
    test('should convert an empty Uint8Array', () => {
        const uint8Array = new Uint8Array([]);
        // @ts-ignore
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('');
    });

    test('should convert a Uint8Array with one byte', () => {
        const uint8Array = new Uint8Array([255]);
        // @ts-ignore
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('/w==');
    });

    test('should convert a Uint8Array with two bytes', () => {
        const uint8Array = new Uint8Array([255, 255]);
        // @ts-ignore
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('//8=');
    });

    test('should convert a Uint8Array with three bytes', () => {
        const uint8Array = new Uint8Array([255, 255, 255]);
        // @ts-ignore
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('////');
    });

    test('should convert a Uint8Array with four bytes', () => {
        const uint8Array = new Uint8Array([72, 101, 108, 108]);
        // @ts-ignore
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('SGVsbA==');
    });
});