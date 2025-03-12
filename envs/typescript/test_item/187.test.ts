// ... (previous code for context)
function merge(arr: number[], l: number, m: number, r: number): void {
    // ... (existing merge function code)

    // Merge the temp arrays back into arr[l..r]
    let i = l, j = m + 1, k = l;
    while (i <= m && j <= r) {
        if (tempArray[i] <= tempArray[j]) {
            arr[k++] = tempArray[i++];
        } else {
            arr[k++] = tempArray[j++];
        }
    }

    // Copy the remaining elements of tempArray[l..m] if any
    while (i <= m) {
        arr[k++] = tempArray[i++];
    }

    // Copy the remaining elements of tempArray[m+1..r] if any
    while (j <= r) {
        arr[k++] = tempArray[j++];
    }
}

function mergeSort(arr: number[], left: number, right: number): void {
    if (left < right) {
        // ... (existing mergeSort function code)
    }
}

// ... (rest of the code)
describe("Merge Sort Test Cases", () => {
    
    test("Sorting an empty array", () => {
        const emptyArray: number[] = [];
        mergeSort(emptyArray, 0, emptyArray.length - 1);
        expect(emptyArray).toEqual([]);
    });

    test("Sorting a single element array", () => {
        const singleElement: number[] = [1];
        mergeSort(singleElement, 0, singleElement.length - 1);
        expect(singleElement).toEqual([1]);
    });

    test("Sorting a sorted array", () => {
        const sortedArray: number[] = [1, 2, 3, 4, 5];
        mergeSort(sortedArray, 0, sortedArray.length - 1);
        expect(sortedArray).toEqual([1, 2, 3, 4, 5]);
    });

    test("Sorting a reverse sorted array", () => {
        const reverseSortedArray: number[] = [5, 4, 3, 2, 1];
        mergeSort(reverseSortedArray, 0, reverseSortedArray.length - 1);
        expect(reverseSortedArray).toEqual([1, 2, 3, 4, 5]);
    });

    test("Sorting an array with random integers", () => {
        const randomArray: number[] = [38, 27, 43, 3, 9, 82, 10];
        const expectedSortedArray: number[] = [3, 9, 10, 27, 38, 43, 82];
        mergeSort(randomArray, 0, randomArray.length - 1);
        expect(randomArray).toEqual(expectedSortedArray);
    });
});
