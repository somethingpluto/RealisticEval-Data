/**
 * Compares two arrays to determine if they contain the same unique elements, irrespective of order.
 * This function utilizes Sets to filter out duplicates and compare the unique elements of both arrays.
 * It returns true if both arrays contain the same elements, without considering the order or frequency of those elements.
 *
 * @param {Array<T>} arr1 - The first array to compare. Elements can be of any type T.
 * @param {Array<T>} arr2 - The second array to compare. Elements should be of the same type as the first array.
 * @returns {boolean} - Returns true if both arrays contain the same unique elements, otherwise returns false.
 *
 * @template T - The type of the elements in the arrays.
 *
 * @example
 * // Returns true as both arrays contain the same numbers
 * compareArrays<number>([1, 2, 2, 3], [3, 1, 2]);
 *
 * // Returns false as the arrays contain different strings
 * compareArrays<string>(['a', 'b'], ['a', 'c']);
 */
function compareArrays<T>(arr1: Array<T>, arr2: Array<T>): boolean {
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);

    if (set1.size !== set2.size) {
        return false;
    }

    for (const item of set1) {
        if (!set2.has(item)) {
            return false;
        }
    }

    return true;
}