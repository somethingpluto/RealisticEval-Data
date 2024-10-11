describe('bitsToBytes', () => {
    test('should convert bits to bytes correctly', () => {
        const bits = [0, 0, 0, 0, 0, 0, 0, 1];
        const expectedOutput = new Uint8Array([1]);
        expect(bitsToBytes(bits)).toEqual(expectedOutput);
    });

    test('should discard incomplete byte if length is not multiple of 8', () => {
        const bits = [0, 0, 0, 0, 0, 0, 1];
        const expectedOutput = new Uint8Array([]);
        expect(bitsToBytes(bits)).toEqual(expectedOutput);
    });
});