type AnyObject = { [key: string]: any };

/**
 * Compares two objects to determine if they have the same depth and structure.
 *
 * @param obj1 - The first object to compare.
 * @param obj2 - The second object to compare.
 * @returns True if the objects have equal depth, otherwise false.
 */
function compareObjectsDepth(obj1: AnyObject, obj2: AnyObject): boolean {
    // Check if both are objects
    if (typeof obj1 !== 'object' || typeof obj2 !== 'object' || obj1 === null || obj2 === null) {
        return false;
    }

    // Get the keys of both objects
    const keys1 = Object.keys(obj1);
    const keys2 = Object.keys(obj2);

    // Check if the number of keys is the same
    if (keys1.length !== keys2.length) {
        return false;
    }

    // Compare each key
    for (const key of keys1) {
        // Check if key exists in both objects
        if (!keys2.includes(key)) {
            return false;
        }

        // Recursively check the depth of the properties
        const isEqualDepth = compareObjectsDepth(obj1[key], obj2[key]);
        if (!isEqualDepth) {
            return false;
        }
    }

    return true;
}