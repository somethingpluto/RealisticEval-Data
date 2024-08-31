/**
 * Sorts an array of objects alphabetically by a specified key.
 *
 * @param {Object[]} array - The array of objects to be sorted.
 * @param {string} key - The key in the objects to sort by.
 * @returns {Object[]} The sorted array based on the specified key.
 */
function sortByKey(array, key) {
    return array.sort((a, b) => {
        // Retrieve the string values from each object by the key, converting to lowercase for case-insensitive comparison
        const valueA = (a[key] || '').toString().toLowerCase();
        const valueB = (b[key] || '').toString().toLowerCase();

        // Compare the values to determine the order
        if (valueA < valueB) {
            return -1; // a comes first
        }
        if (valueA > valueB) {
            return 1; // b comes first
        }
        return 0; // a and b are equal
    });
}