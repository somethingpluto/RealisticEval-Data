/**
 * Sorts an array of objects alphabetically by a specified key.
 *
 * @param {Array<Record<string, any>>} array - The array of objects to be sorted.
 * @param {string} key - The key in the objects to sort by.
 * @returns {Array<Record<string, any>>} The sorted array based on the specified key.
 */
function sortByKey(array: Array<Record<string, any>>, key: string): Array<Record<string, any>> {
    return array.sort((a, b) => {
        const valueA = (a[key] || '').toString().toLowerCase();
        const valueB = (b[key] || '').toString().toLowerCase();

        if (valueA < valueB) {
            return -1; // a comes first
        }
        if (valueA > valueB) {
            return 1; // b comes first
        }
        return 0; // a and b are equal
    });
}