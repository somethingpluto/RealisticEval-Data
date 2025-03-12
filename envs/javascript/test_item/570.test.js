/**
 * Deeply merges two objects.
 * If properties are objects in both objects, they are recursively merged.
 * If a property exists in both objects but is not an object, the value from obj1 is used.
 *
 * @param {Object} obj1 - The first object to merge.
 * @param {Object|null|undefined} obj2 - The second object to merge.
 * @returns {Object} A new object that is the result of the merge.
 */
const deepMergeObjects = (obj1, obj2) => {
    if (obj2 === null || obj2 === undefined) {
        return { ...obj1 };
    }

    const mergedObject = { ...obj1 };

    for (const key in obj2) {
        if (obj2.hasOwnProperty(key)) {
            if (typeof obj2[key] === 'object' && obj2[key] !== null && !Array.isArray(obj2[key])) {
                if (typeof mergedObject[key] === 'object' && mergedObject[key] !== null && !Array.isArray(mergedObject[key])) {
                    mergedObject[key] = deepMergeObjects(mergedObject[key], obj2[key]);
                } else {
                    mergedObject[key] = { ...obj2[key] };
                }
            } else {
                mergedObject[key] = obj2[key];
            }
        }
    }

    return mergedObject;
};
describe('deepMergeObjects', () => {
    test('handles null values in obj2', () => {
        const obj1 = { a: 1, b: 2 };
        const obj2 = null;
        const result = deepMergeObjects(obj1, obj2);
        expect(result).toEqual(obj1); // Should return obj1
    });

    test('handles undefined values in obj2', () => {
        const obj1 = { a: 1, b: 2 };
        const obj2 = undefined;
        const result = deepMergeObjects(obj1, obj2);
        expect(result).toEqual(obj1); // Should return obj1
    });

    test('merges deeply nested objects', () => {
        const obj1 = { a: { b: { c: 1 } }, d: 2 };
        const obj2 = { a: { b: { d: 3 } }, e: 4 };
        const result = deepMergeObjects(obj1, obj2);
        expect(result).toEqual({
            a: {
                b: {
                    c: 1
                }
            },
            d: 2
        });
    });

    test('does not merge arrays but takes them from obj1', () => {
        const obj1 = { a: [1, 2, 3] };
        const obj2 = { a: [4, 5] };
        const result = deepMergeObjects(obj1, obj2);
        expect(result).toEqual({ a: [1, 2, 3] }); // Should keep array from obj1
    });
});
