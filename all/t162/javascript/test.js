describe('boolArrayToBinaryString', () => {
    test('converts an array of all true values', () => {
        const boolArray = [true, true, true];
        const expected = '111';
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('converts an array of all false values', () => {
        const boolArray = [false, false, false];
        const expected = '000';
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('converts an array with a mix of true and false values', () => {
        const boolArray = [true, false, true, false];
        const expected = '1010';
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('handles an empty array', () => {
        const boolArray = [];
        const expected = '';
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('handles a single boolean value', () => {
        const boolArray = [true];
        const expected = '1';
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });
});