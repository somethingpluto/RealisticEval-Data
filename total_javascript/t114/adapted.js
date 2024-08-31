/**
 * Sorts an array of objects by the timestamp property.
 *
 * @param {Object[]} array - The array of objects to be sorted.
 * @returns {Object[]} The sorted array, based on the timestamp property.
 */
function sortByTimestamp(array) {
    return array.sort((a, b) => {
        // Convert timestamp strings to Date objects if necessary
        // and get the time value in milliseconds for comparison.
        const timestampA = new Date(a.timestamp).getTime();
        const timestampB = new Date(b.timestamp).getTime();

        // Sort in ascending order by comparing time values
        return timestampA - timestampB;
    });
}