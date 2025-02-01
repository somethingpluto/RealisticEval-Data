/**
 * Sorts the string array with the shape of "name + number" in ascending order. 
 * If the numbers are the same, sorts by name in ascending order, and returns the sorted array.
 *
 * @param {Array<string>} arr An array of strings to be sorted.
 * @return {Array<string>} A sorted array of strings according to the rules described above.
 */
function sortNames(arr) {
    return arr.sort((a, b) => {
        const [nameA, numberA] = a.split(' ');
        const [nameB, numberB] = b.split(' ');

        if (numberA === numberB) {
            return nameA.localeCompare(nameB);
        }

        return numberA - numberB;
    });
}
describe("sortNames Test Cases", () => {
    // Test Case 2: Same numbers, different names
    test("should sort names with the same numbers in alphabetical order", () => {
        const arr2 = ["Alice10", "Charlie10", "Bob10"];
        const expected2 = ["Alice10", "Bob10", "Charlie10"];
        expect(sortNames(arr2)).toEqual(expected2);
    });

    // Test Case 3: Mixed case with different names and numbers
    test("should sort mixed case names and numbers correctly", () => {
        const arr3 = ["Alice3", "Bob2", "Charlie3", "Bob1"];
        const expected3 = ["Bob1", "Bob2", "Alice3", "Charlie3"];
        expect(sortNames(arr3)).toEqual(expected3);
    });

    // Test Case 4: Single element
    test("should return the same single element array", () => {
        const arr4 = ["Alice5"];
        const expected4 = ["Alice5"];
        expect(sortNames(arr4)).toEqual(expected4);
    });

    // Test Case 5: Empty array
    test("should return an empty array when input is empty", () => {
        const arr5 = [];
        const expected5 = [];
        expect(sortNames(arr5)).toEqual(expected5);
    });
});
