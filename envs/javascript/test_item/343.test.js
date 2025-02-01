/**
 * Compares two objects to determine if they have the same depth and structure.
 *
 * @param obj1 - The first object to compare.
 * @param obj2 - The second object to compare.
 * @returns True if the objects have equal depth, otherwise false.
 */
function compareObjectsDepth(obj1, obj2) {
    if (typeof obj1 !== 'object' || typeof obj2 !== 'object' || obj1 === null || obj2 === null) {
        return false;
    }

    const keys1 = Object.keys(obj1);
    const keys2 = Object.keys(obj2);

    if (keys1.length !== keys2.length) {
        return false;
    }

    for (let key of keys1) {
        if (!keys2.includes(key)) {
            return false;
        }

        const value1 = obj1[key];
        const value2 = obj2[key];

        if (typeof value1 !== typeof value2) {
            return false;
        }

        if (typeof value1 === 'object' && !compareObjectsDepth(value1, value2)) {
            return false;
        }
    }

    return true;
}
describe('compareObjectsDepth function tests', () => {
    test('should return true for equal depth and structure', () => {
        const objA = { a: { b: { c: 1 } }, d: 2 };
        const objB = { a: { b: { c: 3 } }, d: 4 };
        expect(compareObjectsDepth(objA, objB)).toBe(false); // Same structure
    });

    test('should return false for different structure (missing key)', () => {
        const objA = { a: { b: { c: 1 } }, d: 2 };
        const objC = { a: { b: { c: 3 } }, e: 4 };
        expect(compareObjectsDepth(objA, objC)).toBe(false); // Different structure
    });

    test('should return false for different depth', () => {
        const objA = { a: { b: { c: 1 } }, d: 2 };
        const objD = { a: { b: 1 }, d: 2 };
        expect(compareObjectsDepth(objA, objD)).toBe(false); // Different depth
    });

    test('should return false for non-object inputs', () => {
        const objA = { a: { b: { c: 1 } }, d: 2 };
        const objE = null;
        expect(compareObjectsDepth(objA, objE)).toBe(false); // Non-object input
    });

    test('should return false for different types (number vs object)', () => {
        const objA = { a: { b: 1 }, d: 2 };
        const objF = { a: { b: { c: 3 } }, d: 4 };
        expect(compareObjectsDepth(objA, objF)).toBe(false); // Different types
    });

    test('should return true for identical empty objects', () => {
        const objG = {};
        const objH = {};
        expect(compareObjectsDepth(objG, objH)).toBe(true); // Both are empty
    });
});
