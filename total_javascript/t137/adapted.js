/**
 * Merges two objects into one, with properties from the second object
 * potentially overwriting those from the first if there are conflicts.
 *
 * @param {Object} obj1 - The first object.
 * @param {Object} obj2 - The second object.
 * @returns {Object} - The resulting object after merging.
 */
function mergeObjects(obj1, obj2) {
    if (typeof obj1 !== 'object' || obj1 === null || Array.isArray(obj1) ||
        typeof obj2 !== 'object' || obj2 === null || Array.isArray(obj2)) {
        throw new TypeError('Both parameters should be non-null objects and not arrays.');
    }

    return { ...obj1, ...obj2 };
}