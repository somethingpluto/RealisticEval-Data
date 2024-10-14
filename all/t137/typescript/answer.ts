/**
 * Merges two objects into one, with properties from the second object
 * potentially overwriting those from the first if there are conflicts.
 *
 * @param {Record<string, any>} obj1 - The first object.
 * @param {Record<string, any>} obj2 - The second object.
 * @returns {Record<string, any>} - The resulting object after merging.
 */
function mergeObjects(obj1: Record<string, any>, obj2: Record<string, any>): Record<string, any> {
    if (typeof obj1 !== 'object' || obj1 === null || Array.isArray(obj1) ||
        typeof obj2 !== 'object' || obj2 === null || Array.isArray(obj2)) {
        throw new TypeError('Both parameters should be non-null objects and not arrays.');
    }

    return { ...obj1, ...obj2 };
}