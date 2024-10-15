/**
 * Represents an object with a timestamp property.
 */
interface TimestampObject {
    timestamp: string; // Assuming the timestamp is a string
}

/**
 * Sorts an array of objects by the timestamp property.
 *
 * @param {TimestampObject[]} array - The array of objects to be sorted.
 * @returns {TimestampObject[]} The sorted array, based on the timestamp property.
 */
function sortByTimestamp(array: TimestampObject[]): TimestampObject[] {
    return array.sort((a, b) => {
        // Convert timestamp strings to Date objects
        const timestampA = new Date(a.timestamp).getTime();
        const timestampB = new Date(b.timestamp).getTime();

        // Sort in ascending order by comparing time values
        return timestampA - timestampB;
    });
}