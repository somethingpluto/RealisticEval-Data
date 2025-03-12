/**
 * Produces all combinations of numeric arrays for each key in the given map object and returns them as a two-dimensional array
 *
 * @param {Map<string, number[]>} map - A map where each key is a string, and each value is an array of numbers.
 * @returns {number[][]} An array of arrays, where each sub-array is a unique combination of numbers from the Map's values.
 */
function generateCombinations(map) {
    // Helper function to generate combinations recursively
    function combine(currentCombination, keys) {
        if (keys.length === 0) {
            return [currentCombination];
        }

        const key = keys[0];
        const values = map.get(key);
        const remainingKeys = keys.slice(1);

        let result = [];
        for (const value of values) {
            const newCombination = currentCombination.concat(value);
            result = result.concat(combine(newCombination, remainingKeys));
        }

        return result;
    }

    // Start the combination process with an empty array and all keys
    const keys = Array.from(map.keys());
    return combine([], keys);
}
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
