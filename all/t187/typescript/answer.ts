function merge(arr: number[], left: number, mid: number, right: number): void {
    const n1 = mid - left + 1; // Size of the left subarray
    const n2 = right - mid;    // Size of the right subarray

    // Create temporary arrays
    const L: number[] = new Array(n1);
    const R: number[] = new Array(n2);

    // Copy data to temporary arrays L[] and R[]
    for (let i = 0; i < n1; i++) {
        L[i] = arr[left + i];
    }
    for (let j = 0; j < n2; j++) {
        R[j] = arr[mid + 1 + j];
    }

    // Merge the temporary arrays back into arr[left..right]
    let i = 0; // Initial index of the first subarray
    let j = 0; // Initial index of the second subarray
    let k = left; // Initial index to be sorted

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[], if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[], if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

function mergeSort(arr: number[], left: number, right: number): void {
    if (left < right) {
        const mid = left + Math.floor((right - left) / 2);

        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}