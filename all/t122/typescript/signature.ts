/**
 * Safely splices an array by removing a specified number of elements from a given index,
 * and optionally replaces them with a new element.
 *
 * @param {T[]} inputArray - The original array to be modified.
 * @param {number} amountToRemove - The number of elements to remove from the array.
 * @param {number} indexToRemove - The index at which to start removing elements.
 * @param {T} [replaceWith] - Optional. The element to replace the removed elements with.
 * @returns {T[]} - A new array with the specified elements removed and optionally replaced.
 */
function safeSplice<T>(
    inputArray: T[],
    amountToRemove: number,
    indexToRemove: number,
    replaceWith?: T
): T[] {
    // function implementation
}