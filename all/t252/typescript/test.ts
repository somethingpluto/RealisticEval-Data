describe('BitSequenceEncoder', () => {
    it('should convert integer values of "bits" key to binary strings', () => {
        const encoder = new BitSequenceEncoder();
        const input = { bits: 255 };
        const expectedOutput = '{"bits":"11111111"}';

        const result = encoder.encode(input);

        expect(result).toBe(expectedOutput);
    });

    it('should leave other keys unchanged', () => {
        const encoder = new BitSequenceEncoder();
        const input = { bits: 255, otherKey: 'otherValue' };
        const expectedOutput = '{"bits":"11111111","otherKey":"otherValue"}';

        const result = encoder.encode(input);

        expect(result).toBe(expectedOutput);
    });

    it('should handle multiple "bits" keys correctly', () => {
        const encoder = new BitSequenceEncoder();
        const input = { bits: 255, anotherBits: 16 };
        const expectedOutput = '{"bits":"11111111","anotherBits":"00010000"}';

        const result = encoder.encode(input);

        expect(result).toBe(expectedOutput);
    });
});