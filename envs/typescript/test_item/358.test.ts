import { parse } from 'path';

function sortNames(arr: string[]): string[] {
  return arr.sort((a, b) => {
    const [nameA, numA] = parse(a).name.split(/_/).join('').split(/(\d+)/).filter(Boolean);
    const [nameB, numB] = parse(b).name.split(/_/).join('').split(/(\d+)/).filter(Boolean);

    const numberComparison = parseInt(numA, 10) - parseInt(numB, 10);
    if (numberComparison !== 0) return numberComparison;

    return nameA.localeCompare(nameB);
  });
}
describe("sortNames Test Cases", () => {
    // Test Case 2: Same numbers, different names
    test("Same numbers, different names", () => {
        const arr2 = ["Alice10", "Charlie10", "Bob10"];
        const expected2 = ["Alice10", "Bob10", "Charlie10"];
        expect(sortNames(arr2)).toEqual(expected2);
    });

    // Test Case 3: Mixed case with different names and numbers
    test("Mixed case with different names and numbers", () => {
        const arr3 = ["Alice3", "Bob2", "Charlie3", "Bob1"];
        const expected3 = ["Bob1", "Bob2", "Alice3", "Charlie3"];
        expect(sortNames(arr3)).toEqual(expected3);
    });

    // Test Case 4: Single element
    test("Single element", () => {
        const arr4 = ["Alice5"];
        const expected4 = ["Alice5"];
        expect(sortNames(arr4)).toEqual(expected4);
    });

    // Test Case 5: Empty array
    test("Empty array", () => {
        const arr5: string[] = [];
        const expected5: string[] = [];
        expect(sortNames(arr5)).toEqual(expected5);
    });
});
