/**
 * Sorts an array of integers using the Hill Sort (Shell Sort) algorithm.
 *
 * @param arr An array of integers that will be sorted in-place.
 *
 */
function hillSort(arr: number[]): void {
    let n = arr.length;
    let gap = Math.floor(n / 2);

    while (gap > 0) {
        for (let i = gap; i < n; i++) {
            let temp = arr[i];
            let j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            arr[j] = temp;
        }
        gap = Math.floor(gap / 2);
    }
}

// Unit tests
function testHillSort() {
    let testCases = [
        { input: [3, 1, 4, 1, 5, 9, 2, 6], expected: [1, 1, 2, 3, 4, 5, 6, 9] },
        { input: [], expected: [] },
        { input: [5], expected: [5] },
        { input: [1, 2, 3, 4, 5], expected: [1, 2, 3, 4, 5] },
        { input: [5, 4, 3, 2, 1], expected: [1, 2, 3, 4, 5] },
    ];

    testCases.forEach((testCase, index) => {
        hillSort(testCase.input);
        console.assert(
            JSON.stringify(testCase.input) === JSON.stringify(testCase.expected),
            `Test case ${index + 1} failed: expected ${testCase.expected}, got ${testCase.input}`
        );
        console.log(`Test case ${index + 1} passed`);
    });
}

testHillSort();
function isSorted(arr: number[]): boolean {
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < arr[i - 1]) {
            return false;
        }
    }
    return true;
}

// Test cases for Hill Sort
describe("Hill Sort", () => {
    test("Sort an already sorted array", () => {
        const arr = [1, 2, 3, 4, 5];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test("Sort an array in reverse order", () => {
        const arr = [5, 4, 3, 2, 1];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test("Sort an array with duplicate values", () => {
        const arr = [3, 1, 2, 3, 2];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test("Sort an array with all identical values", () => {
        const arr = [1, 1, 1, 1, 1];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test("Sort an empty array", () => {
        const arr: number[] = [];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test("Sort an array with one element", () => {
        const arr = [42];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test("Sort a large random array", () => {
        const arr = [3, 7, 2, 5, 1, 4, 6, 0, 9, 8];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });
});
