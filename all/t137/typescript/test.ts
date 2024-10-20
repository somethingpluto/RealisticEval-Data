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