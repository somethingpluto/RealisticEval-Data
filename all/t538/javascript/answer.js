/**
 * Sorts an array of objects alphabetically based on a specified field.
 * @param {Array} array - The array of objects to sort.
 * @param {String} field - The field of the objects to sort by.
 * @param {Boolean} ascending - If true, sort in ascending order; if false, sort in descending order.
 * @returns {Array} - The sorted array of objects.
 */
function sortByField(array, field, ascending = true) {
    // Check if the field exists in the first object to avoid errors
    if (array.length === 0 || !array[0].hasOwnProperty(field)) {
        throw new Error('Field does not exist in the objects.');
    }

    // Sorting function
    return array.sort((a, b) => {
        const valueA = a[field].toString().toLowerCase();
        const valueB = b[field].toString().toLowerCase();

        if (valueA < valueB) {
            return ascending ? -1 : 1; // Ascending order: a comes before b; Descending order: b comes before a
        }
        if (valueA > valueB) {
            return ascending ? 1 : -1; // Ascending order: b comes before a; Descending order: a comes before b
        }
        return 0; // They are equal
    });
}
