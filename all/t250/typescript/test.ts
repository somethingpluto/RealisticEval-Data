describe('invertDictionary', () => {
    it('should invert a simple dictionary', () => {
        const input = { a: 1, b: 2 };
        const expectedOutput = { 1: ['a'], 2: ['b'] };
        expect(invertDictionary(input)).toEqual(expectedOutput);
    });

    it('should handle multiple keys with the same value', () => {
        const input = { a: 1, b: 1, c: 2 };
        const expectedOutput = { 1: ['a', 'b'], 2: ['c'] };
        expect(invertDictionary(input)).toEqual(expectedOutput);
    });

    it('should handle empty dictionary', () => {
        const input = {};
        const expectedOutput = {};
        expect(invertDictionary(input)).toEqual(expectedOutput);
    });
});