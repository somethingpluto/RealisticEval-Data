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