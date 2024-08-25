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
/**
 * Produces all combinations of numeric arrays for each key in the given map object and returns them as a two-dimensional array
 *
 * @param {Map<string, number[]>} map - A map where each key is a string, and each value is an array of numbers.
 * @returns {number[][]} An array of arrays, where each sub-array is a unique combination of numbers from the Map's values.
 */
function generateCombinations(map: Map<string, number[]>): number[][] {
    const keys = Array.from(map.keys());
    const values = Array.from(map.values());

    const combinations: number[][] = [];

    /**
     * Helper function to recursively generate combinations.
     *
     * @param {number[]} currentCombination - The current combination being built.
     * @param {number} currentIndex - The current index in the keys/values arrays.
     */
    function generate(currentCombination: number[], currentIndex: number): void {
        // Base case: If we've reached the end of the keys, push the combination to the result.
        if (currentIndex === keys.length) {
            combinations.push(currentCombination.slice());
            return;
        }

        // Recursively generate combinations for the current key's values.
        const currentValues = values[currentIndex];
        for (const value of currentValues) {
            currentCombination[currentIndex] = value;
            generate(currentCombination, currentIndex + 1);
        }
    }

    // Start the recursive combination generation.
    generate([], 0);
    return combinations;
}