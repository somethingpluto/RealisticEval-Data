// ... (previous code for context)
function mergeObjects(obj1: Record<string, any>, obj2: Record<string, any>): Record<string, any> {
  // ... (existing code)
}

// Unit tests
describe('mergeObjects', () => {
  it('should merge objects with no conflicts', () => {
    const obj1 = { a: 1, b: 2 };
    const obj2 = { c: 3 };
    const result = mergeObjects(obj1, obj2);
    expect(result).toEqual({ a: 1, b: 2, c: 3 });
  });

  it('should overwrite properties in obj1 with properties from obj2', () => {
    const obj1 = { a: 1, b: 2 };
    const obj2 = { b: 3, c: 4 };
    const result = mergeObjects(obj1, obj2);
    expect(result).toEqual({ a: 1, b: 3, c: 4 });
  });

  it('should handle nested objects', () => {
    const obj1 = { a: { x: 1 } };
    const obj2 = { a: { y: 2 } };
    const result = mergeObjects(obj1, obj2);
    expect(result).toEqual({ a: { x: 1, y: 2 } });
  });

  it('should handle arrays', () => {
    const obj1 = { a: [1, 2] };
    const obj2 = { a: [3, 4] };
    const result = mergeObjects(obj1, obj2);
    expect(result).toEqual({ a: [1, 2, 3, 4] });
  });
});
// ... (rest of the code)
describe('mergeObjects', () => {
    test('correctly merges two objects with non-conflicting keys', () => {
        const obj1: Record<string, any> = { name: "Alice" };
        const obj2: Record<string, any> = { age: 30 };
        const expected: Record<string, any> = { name: "Alice", age: 30 };
        expect(mergeObjects(obj1, obj2)).toEqual(expected);
    });

    test('properties from the second object overwrite properties from the first', () => {
        const obj1: Record<string, any> = { name: "Alice", age: 25 };
        const obj2: Record<string, any> = { age: 30 };
        const expected: Record<string, any> = { name: "Alice", age: 30 };
        expect(mergeObjects(obj1, obj2)).toEqual(expected);
    });

    test('merges objects with nested structures correctly', () => {
        const obj1: Record<string, any> = { user: { name: "Alice", age: 25 } };
        const obj2: Record<string, any> = { user: { age: 30 } };
        const expected: Record<string, any> = { user: { age: 30 } };  // Note: obj2 does not merge deeply, it replaces the entire 'user' object
        expect(mergeObjects(obj1, obj2)).toEqual(expected);
    });
});
