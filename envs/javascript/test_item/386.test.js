function findCommonElements(arr1, arr2) {
    const commonElements = [];
    const set1 = new Set(arr1);

    for (const elem of arr2) {
        if (set1.has(elem)) {
            commonElements.push(elem);
        }
    }

    return commonElements;
}

