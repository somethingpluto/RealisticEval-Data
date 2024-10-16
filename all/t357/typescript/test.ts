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