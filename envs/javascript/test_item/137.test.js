/**
 * Merges two objects into one, with properties from the second object
 * potentially overwriting those from the first if there are conflicts.
 *
 * @param {Object} obj1 - The first object.
 * @param {Object} obj2 - The second object.
 * @returns {Object} - The resulting object after merging.
 */
function mergeObjects(obj1, obj2) {
    // Create a new object to hold the merged properties
    const mergedObject = {};

    // Copy all properties from obj1 to the mergedObject
    for (let key in obj1) {
        if (obj1.hasOwnProperty(key)) {
            mergedObject[key] = obj1[key];
        }
    }

    // Copy all properties from obj2 to the mergedObject, potentially overwriting existing properties
    for (let key in obj2) {
        if (obj2.hasOwnProperty(key)) {
            mergedObject[key] = obj2[key];
        }
    }

    return mergedObject;
}
describe('mergeObjects', () => {
    test('correctly merges two objects with non-conflicting keys', () => {
        const obj1 = { name: "Alice" };
        const obj2 = { age: 30 };
        const expected = { name: "Alice", age: 30 };
        expect(mergeObjects(obj1, obj2)).toEqual(expected);
    });

    test('properties from the second object overwrite properties from the first', () => {
        const obj1 = { name: "Alice", age: 25 };
        const obj2 = { age: 30 };
        const expected = { name: "Alice", age: 30 };
        expect(mergeObjects(obj1, obj2)).toEqual(expected);
    });

    test('merges objects with nested structures correctly', () => {
        const obj1 = { user: { name: "Alice", age: 25 } };
        const obj2 = { user: { age: 30 } };
        const expected = { user: { age: 30 } };  // Note: obj2 does not merge deeply, it replaces the entire 'user' object
        expect(mergeObjects(obj1, obj2)).toEqual(expected);
    });
});
