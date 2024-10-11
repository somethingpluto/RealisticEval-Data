/**
 * Iterates through the array of elements until the first null is encountered,
 * returning a new array that includes all elements before the null.
 *
 * @param {Array} array - The array to iterate through.
 * @returns {Array} - A new array containing elements before the first null.
 */
function elementsBeforeNull(array) {
    const result = []; // Initialize an empty array to hold the result

    for (let i = 0; i < array.length; i++) {
        if (array[i] === null) {
            break; // Exit the loop if null is encountered
        }
        result.push(array[i]); // Add the current element to the result array
    }

    return result; // Return the result array
}