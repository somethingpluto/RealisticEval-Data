describe('generateCombinations', () => {
    test('generates combinations for a single key with multiple values', () => {
        const map = new Map<string, number[]>([['a', [1, 2, 3]]]);
        const expected = [[1], [2], [3]];
        // @ts-ignore
        expect(generateCombinations(map)).toEqual(expected);
    });

    test('generates combinations for multiple keys with single values', () => {
        const map = new Map<string, number[]>([['a', [1]], ['b', [2]]]);
        const expected = [[1, 2]];
        // @ts-ignore
        expect(generateCombinations(map)).toEqual(expected);
    });

    test('generates combinations for multiple keys with multiple values', () => {
        const map = new Map<string, number[]>([['a', [1, 2]], ['b', [3, 4]]]);
        const expected = [
            [1, 3], [1, 4],
            [2, 3], [2, 4]
        ];
        // @ts-ignore
        expect(generateCombinations(map)).toEqual(expected);
    });

    test('handles an empty map', () => {
        const map = new Map<string, number[]>();
        const expected: number[][] = [[]];
        // @ts-ignore
        expect(generateCombinations(map)).toEqual(expected);
    });

    test('handles keys with empty arrays as values', () => {
        const map = new Map<string, number[]>([['a', []], ['b', [1, 2]]]);
        const expected: number[][] = [];
        // @ts-ignore
        expect(generateCombinations(map)).toEqual(expected);
    });
});