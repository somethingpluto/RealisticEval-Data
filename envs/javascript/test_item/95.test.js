/**
 * Finds matching elements and their indices in the input array
 * based on the specified comparison function.
 *
 * @param {Array} arr - The input array to search through.
 * @param {Function} comparisonFn - The comparison function to determine matches.
 * @returns {Array} - An array of objects, each containing the matched element and its index.
 */
function findMatchingElements(arr, comparisonFn) {
    const matches = [];
    for (let i = 0; i < arr.length; i++) {
        if (comparisonFn(arr[i])) {
            matches.push({ element: arr[i], index: i });
        }
    }
    return matches;
}
describe('findMatchingElements', () => {
    test('should return an empty array for an empty input array', () => {
        const result = findMatchingElements([], (el) => el > 0);
        expect(result).toEqual([]);
    });

    test('should return matching elements and their indices', () => {
        const inputArray = [1, 2, 3, 4, 5];
        const comparisonFunction = (num) => num > 3;
        const result = findMatchingElements(inputArray, comparisonFunction);
        expect(result).toEqual([
            {element: 4, index: 3},
            {element: 5, index: 4},
        ]);
    });

    test('should return elements that are strings matching a specific condition', () => {
        const inputArray = ['apple', 'banana', 'cherry', 'date'];
        const comparisonFunction = (fruit) => fruit.startsWith('b');
        const result = findMatchingElements(inputArray, comparisonFunction);
        expect(result).toEqual([
            {element: 'banana', index: 1},
        ]);
    });

    test('should return multiple elements with the same value', () => {
        const inputArray = [1, 2, 2, 3, 2, 4];
        const comparisonFunction = (num) => num === 2;
        const result = findMatchingElements(inputArray, comparisonFunction);
        expect(result).toEqual([
            {element: 2, index: 1},
            {element: 2, index: 2},
            {element: 2, index: 4},
        ]);
    });

    test('should return matching objects based on a property', () => {
        const inputArray = [
            {name: 'Alice', age: 25},
            {name: 'Bob', age: 30},
            {name: 'Charlie', age: 30},
        ];
        const comparisonFunction = (person) => person.age === 30;
        const result = findMatchingElements(inputArray, comparisonFunction);
        expect(result).toEqual([
            {element: {name: 'Bob', age: 30}, index: 1},
            {element: {name: 'Charlie', age: 30}, index: 2},
        ]);
    });

    test('should return no elements if no matches found', () => {
        const inputArray = [1, 3, 5, 7];
        const comparisonFunction = (num) => num % 2 === 0; // looking for even numbers
        const result = findMatchingElements(inputArray, comparisonFunction);
        expect(result).toEqual([]);
    });

    test('should work with a comparison function that checks for negative numbers', () => {
        const inputArray = [-1, -2, 0, 1, 2];
        const comparisonFunction = (num) => num < 0;
        const result = findMatchingElements(inputArray, comparisonFunction);
        expect(result).toEqual([
            {element: -1, index: 0},
            {element: -2, index: 1},
        ]);
    });
});
