// written by ChatGPT... weirdly.

/**
 * Compares two arrays, returns true if they contain the same contents
 * @param arr1
 * @param arr2
 */
export function compareArrays<T>(arr1: Array<T>, arr2: Array<T>): boolean {
    if (arr1.length !== arr2.length) {
        return false;
    }

    const set1 = new Set(arr1);
    const set2 = new Set(arr2);

    for (const contents of set1) {
        if (!set2.has(contents)) {
            return false;
        }
    }

    return true;
}