/**
 * Removes the first occurrence of a specified element from an array.
 *
 * @param {Array<T>} array - The array from which to remove the element.
 * @param {T} element - The element to remove from the array.
 * @returns {Array<T>} A new array with the element removed, or the original array if the element is not found.
 */
function removeElementInArray<T>(array: Array<T>, element: T): Array<T> {
    const newArray: T[] = [];

    for (let index = 0; index < array.length; index++) {
        if (array[index] !== element) {
            newArray.push(array[index]);
        }
    }

    return newArray;
}