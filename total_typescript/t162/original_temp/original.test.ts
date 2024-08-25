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
function boolArrayToBinaryString(boolArray: boolean[]): string {
    let binaryStr = "";
    boolArray.forEach((bool, index) => {
      binaryStr += bool ? "1" : "0";
    });
    return binaryStr;
  }
  