function insertionSort(arr: number[]): void {
    const n: number = arr.length;
    for (let i = 1; i < n; i++) {
        const key: number = arr[i];
        let j: number = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}