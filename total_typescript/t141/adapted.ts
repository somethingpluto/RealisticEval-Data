function compareArrays<T>(arr1: Array<T>, arr2: Array<T>): boolean {

    // Create sets from both arrays to eliminate duplicates and enable fast lookup
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);

    // If the sizes of the sets are different, the arrays can't contain the same elements
    if (set1.size !== set2.size) {
        return false;
    }

    // Check if all elements in set1 are present in set2
    // @ts-ignore
    for (const item of set1) {
        if (!set2.has(item)) {
            return false;
        }
    }

    // If all checks passed, the arrays contain the same elements
    return true;
}