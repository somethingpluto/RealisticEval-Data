describe('generateCombinations', () => {
    
    test('empty input', () => {
        const inputData = [];
        const expected = [];
        expect(generateCombinations(inputData)).toEqual(expected); // Jest's expect is similar to unittest's assertEqual
    });

    test('single empty list', () => {
        const inputData = [[]]; // Equivalent to [[]] in Python
        const expected = [];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

    test('single non-empty list', () => {
        const inputData = [["a", "b", "c"]]; // Same representation in JavaScript
        const expected = [["a"], ["b"], ["c"]];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

    test('multiple lists', () => {
        const inputData = [["a", "b"], ["1", "2"]]; // Same representation in JavaScript
        const expected = [["a", "1"], ["a", "2"], ["b", "1"], ["b", "2"]];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

    test('input containing empty list', () => {
        const inputData = [["a", "b"], [], ["1", "2"]]; // Same representation in JavaScript
        const expected = [];
        expect(generateCombinations(inputData)).toEqual(expected);
    });

});