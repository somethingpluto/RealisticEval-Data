/**
 * Removes the first occurrence of a specified element from an array.
 *
 * @param {Array} array - The array from which to remove the element.
 * @param {*} element - The element to remove from the array.
 * @returns {Array} A new array with the element removed, or the original array if the element is not found.
 */
function removeElementInArray(array, element) {
    // Create a new array to avoid modifying the original
    const newArray = [];

    // Iterate through the original array
    for (let index = 0; index < array.length; index++) {
        if (array[index] !== element) {
            newArray.push(array[index]); // Add elements that are not the target element
        }
    }

    // Return a new array that does not include the specified element
    return newArray;
}