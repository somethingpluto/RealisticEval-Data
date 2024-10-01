/**
 * Sorts an array of strings alphabetically based on a specified field.
 *
 * @param {Array} arr - The array of objects to be sorted.
 * @param {Function} getField - A function to extract the field for comparison.
 * @param {boolean} [ascending=true] - Whether to sort in ascending order.
 * @returns {Array} - The sorted array.
 */
function sortAlphabetically(arr, getField, ascending = true) {
    return arr.slice().sort((a, b) => {
        const fieldA = getField(a).toLowerCase();
        const fieldB = getField(b).toLowerCase();

        if (fieldA < fieldB) return -1;
        if (fieldA > fieldB) return 1;
        return 0;
    }).reverse(!ascending); // Reverse the sorted array if not ascending
}