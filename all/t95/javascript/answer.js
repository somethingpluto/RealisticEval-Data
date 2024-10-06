/**
 * Finds matching elements and their indices in the input array
 * based on the specified comparison function.
 *
 * @param {Array} arr - The input array to search through.
 * @param {Function} comparisonFn - The comparison function to determine matches.
 * @returns {Array} - An array of objects, each containing the matched element and its index.
 */
function findMatchingElements(arr, comparisonFn) {
    const result = [];

    for (let i = 0; i < arr.length; i++) {
        if (comparisonFn(arr[i])) {
            result.push({ element: arr[i], index: i });
        }
    }

    return result;
}