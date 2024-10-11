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
}