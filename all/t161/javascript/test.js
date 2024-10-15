describe('generateCombinations', () => {
    test('generates combinations for a single key with multiple values', () => {
        const map = new Map([['a', [1, 2, 3]]]);
        const expected = [[1], [2], [3]];
        expect(generateCombinations(map)).toEqual(expected);
    });

    test('generates combinations for multiple keys with single values', () => {
        const map = new Map([['a', [1]], ['b', [2]]]);
        const expected = [[1, 2]];
        expect(generateCombinations(map)).toEqual(expected);
    });

    test('generates combinations for multiple keys with multiple values', () => {
        const map = new Map([['a', [1, 2]], ['b', [3, 4]]]);
        const expected = [
            [1, 3], [1, 4],
            [2, 3], [2, 4]
        ];
        expect(generateCombinations(map)).toEqual(expected);
    });

    test('handles an empty map', () => {
        const map = new Map();
        const expected = [[]];
        expect(generateCombinations(map)).toEqual(expected);
    });

    test('handles keys with empty arrays as values', () => {
        const map = new Map([['a', []], ['b', [1, 2]]]);
        const expected = [];
        expect(generateCombinations(map)).toEqual(expected);
    });
});