/**
 * Implement a function that performs Shell sort on an array
 * @param arr - The array to be sorted
 */
function shellSort(arr: number[]): void {
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
describe("Shell sort - Basic functionality", () => {
    test("Test Case 1: Already sorted array", () => {
        const arr = [1, 2, 3, 4, 5];
        shellSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test("Test Case 2: Reverse sorted array", () => {
        const arr = [5, 4, 3, 2, 1];
        shellSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test("Test Case 3: Array with duplicate elements", () => {
        const arr = [4, 2, 2, 4, 1];
        shellSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test("Test Case 4: Array with negative numbers", () => {
        const arr = [-3, -1, -4, -2, 0];
        shellSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test("Test Case 5: Empty array", () => {
        const arr: number[] = [];
        shellSort(arr);
        expect(isSorted(arr)).toBe(true);
    });
});
