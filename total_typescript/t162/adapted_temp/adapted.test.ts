describe('boolArrayToBinaryString', () => {
    test('converts an array of all true values', () => {
        const boolArray = [true, true, true];
        const expected = '111';
        // @ts-ignore
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('converts an array of all false values', () => {
        const boolArray = [false, false, false];
        const expected = '000';
        // @ts-ignore
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('converts an array with a mix of true and false values', () => {
        const boolArray = [true, false, true, false];
        const expected = '1010';
        // @ts-ignore
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('handles an empty array', () => {
        const boolArray: boolean[] = [];
        const expected = '';
        // @ts-ignore
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('handles a single boolean value', () => {
        const boolArray = [true];
        const expected = '1';
        // @ts-ignore
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });
});
/**
 * Converts the array of Boolean values to a binary string representation, which converts to the character 1 if the Boolean value is true. Otherwise, it is converted to the character 0, and the final string is returned
 *
 * @param {boolean[]} boolArray - An array of boolean values.
 * @returns {string} A binary string where '1' represents true and '0' represents false.
 */
function boolArrayToBinaryString(boolArray: boolean[]): string {
    return boolArray.map(bool => (bool ? "1" : "0")).join("");
}
