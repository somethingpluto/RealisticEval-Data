type PlainObject = { [key: string]: any };

/**
 * Deeply merges two objects.
 * If properties are objects in both objects, they are recursively merged.
 * If a property exists in both objects but is not an object, the value from obj1 is used.
 *
 * @param obj1 - The first object to merge.
 * @param obj2 - The second object to merge.
 * @returns A new object that is the result of the merge.
 */
const deepMergeObjects = (obj1: PlainObject, obj2: PlainObject | null | undefined): PlainObject => {
    // Return obj1 if obj2 is null or undefined
    if (obj2 == null) {
        return obj1;
    }

    // Create a shallow copy of obj2 to be modified
    const output: PlainObject = { ...obj2 };

    // Iterate through the keys of obj1
    for (const key of Object.keys(obj1)) {
        if (obj1.hasOwnProperty(key)) {
            const value1 = obj1[key];
            const value2 = obj2[key];

            // Check if both values are objects
            if (value1 && typeof value1 === "object" && value2 && typeof value2 === "object") {
                // Recursively merge objects
                output[key] = deepMergeObjects(value1, value2);
            } else {
                // Use the value from obj1
                output[key] = value1;
            }
        }
    }

    return output;
};
