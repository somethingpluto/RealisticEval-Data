/**
 * Returns the object from the list with the given ID, or null if it is not present
 *
 * @param {string | number} id - The `id` to search for in the list.
 * @param {Array<{ id?: string | number; [key: string]: any }>} list - The list of objects to search through.
 * @returns {Object | null} The object with the matching `id`, or `null` if no match is found.
 */
function getObjectById(id: string | number, list: Array<{ id?: string | number; [key: string]: any }>): { id: string | number } | null {
    for (const obj of list) {
        if ('id' in obj && obj.id === id) {
            return obj;
        }
    }
    return null;
}