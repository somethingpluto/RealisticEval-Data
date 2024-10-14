/**
 * Finds matching elements and their indices in the input array
 * based on the specified comparison function.
 *
 * @param {Array<T>} arr - The input array to search through.
 * @param {(element: T) => boolean} comparisonFn - The comparison function to determine matches.
 * @returns {Array<{ element: T; index: number }>} - An array of objects, each containing the matched element and its index.
 */
function findMatchingElements<T>(arr: T[], comparisonFn: (element: T) => boolean): Array<{ element: T; index: number }> {
}