describe('generateCombinations', () => {
    
    test('should return an empty array for empty input', () => {
        const inputData: Array<Array<string>> = [];
        const expected: Array<Array<string>> = [];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

    test('should return an empty array for a single empty list', () => {
        const inputData: Array<Array<string>> = [[]];
        const expected: Array<Array<string>> = [];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

    test('should return combinations for a single non-empty list', () => {
        const inputData: Array<Array<string>> = [['a', 'b', 'c']];
        const expected: Array<Array<string>> = [['a'], ['b'], ['c']];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

    test('should return combinations for multiple lists', () => {
        const inputData: Array<Array<string>> = [['a', 'b'], ['1', '2']];
        const expected: Array<Array<string>> = [['a', '1'], ['a', '2'], ['b', '1'], ['b', '2']];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

    test('should return an empty array for input containing an empty list', () => {
        const inputData: Array<Array<string>> = [['a', 'b'], [], ['1', '2']];
        const expected: Array<Array<string>> = [];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

});