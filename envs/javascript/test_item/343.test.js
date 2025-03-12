/**
 * Compares two objects to determine if they have the same depth and structure.
 *
 * @param obj1 - The first object to compare.
 * @param obj2 - The second object to compare.
 * @returns True if the objects have equal depth, otherwise false.
 */
function compareObjectsDepth(obj1, obj2) {
    // Helper function to get the depth of an object
    function getObjectDepth(obj) {
        if (typeof obj !== 'object' || obj === null) {
            return 0;
        }
        let maxDepth = 0;
        for (let key in obj) {
            if (obj.hasOwnProperty(key)) {
                const depth = getObjectDepth(obj[key]);
                if (depth > maxDepth) {
                    maxDepth = depth;
                }
            }
        }
        return maxDepth + 1;
    }

    // Get the depth of both objects
    const depth1 = getObjectDepth(obj1);
    const depth2 = getObjectDepth(obj2);

    // Compare the depths
    return depth1 === depth2;
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
