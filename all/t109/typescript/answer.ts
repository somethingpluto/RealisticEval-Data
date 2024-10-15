/**
 * Represents an object in the list.
 */
interface IdentifiableObject {
    id: string | number;
    [key: string]: any; // Allows for additional properties
}

/**
 * Returns the object from the list with the given ID, or null if it is not present.
 *
 * @param {string | number} id - The `id` to search for in the list.
 * @param {Array<IdentifiableObject>} list - The list of objects to search through.
 * @returns {IdentifiableObject | null} The object with the matching `id`, or `null` if no match is found.
 */
function getObjectById(id: string | number, list: IdentifiableObject[]): IdentifiableObject | null {
    // Iterate over the list of objects
    for (let i = 0; i < list.length; i++) {
        const obj = list[i];

        // Check if the object has an `id` property that matches the given id
        if (obj.id === id) {
            // If a match is found, return the object
            return obj;
        }
    }

    // If no match is found, return null
    return null;
}