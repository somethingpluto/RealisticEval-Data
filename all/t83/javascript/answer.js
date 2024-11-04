/**
 * Rotate the elements of the array to the left by one position. The first element
 * is moved to the end of the array, and all other elements are shifted one position to the left.
 *
 * @param {number[]} elements - An array of numbers to be rotated.
 * @returns {number[]} The rotated array with elements shifted to the left by one position.
 */
function rotateListElements(elements) {
    if (elements.length > 1) {
        elements = elements.slice(1).concat([elements[0]]);
    }
    return elements;
}
/**
 * Rotate the elements of the array, moving the first element to the end and shifting all others forward.
 *
 * @param {Array} elements - The array of elements to rotate.
 * @returns {Array} The array after rotation.
 */
function rotateList(elements) {
    if (!elements.length) {
        return elements; // Return the array as is if it's empty
    }
    const rotatedList = elements.slice(1).concat(elements[0]);
    return rotatedList;
}