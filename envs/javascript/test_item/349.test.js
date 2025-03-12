/**
 * Generates all possible combinations of elements from a list of lists.
 * Each combination consists of picking exactly one element from each list in the input list of lists.
 * This method is useful for generating product variations, scenarios in decision-making tools,
 * or any context where all possible combinations of a set of options need to be explored.
 *
 * @param {Array<Array<any>>} inputLists - A list of lists containing the elements to combine.
 *                                          The lists must not be empty but can contain elements of any type.
 * @returns {Array<Array<any>>} - A list of lists, where each inner list represents a possible combination of elements
 *                                 taken from the input lists. Returns an empty list if the input list is empty.
 */
function generateCombinations(inputLists) {
    if (inputLists.length === 0) {
        return [];
    }

    function combine(lists, index) {
        if (index === lists.length) {
            return [[]];
        }

        const currentList = lists[index];
        const remainingCombinations = combine(lists, index + 1);
        const combinations = [];

        for (const element of currentList) {
            for (const combination of remainingCombinations) {
                combinations.push([element, ...combination]);
            }
        }

        return combinations;
    }

    return combine(inputLists, 0);
}
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
