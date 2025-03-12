type AnyObject = { [key: string]: any };// ... (previous code for context)

function compareObjectsDepth(obj1: AnyObject, obj2: AnyObject, depth = 0, maxDepth = 100): boolean {
  if (depth > maxDepth) {
    return true; // Prevents infinite loops by stopping after maxDepth
  }

  // ... (rest of the function remains unchanged)

  // Recursively compare nested objects
  for (const key in obj1) {
    if (!(key in obj2)) {
      return false;
    }
    if (!compareObjectsDepth(obj1[key], obj2[key], depth + 1, maxDepth)) {
      return false;
    }
  }

  // ... (rest of the function remains unchanged)
}

// ... (rest of the code for context)
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
