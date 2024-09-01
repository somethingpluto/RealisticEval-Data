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

    test('throws TypeError if either input is not an object', () => {
        const obj1 = "not an object";
        const obj2 = { valid: true };
        expect(() => mergeObjects(obj1, obj2)).toThrow(TypeError);
        expect(() => mergeObjects(obj2, obj1)).toThrow(TypeError);
    });

    test('handles null and arrays correctly by throwing TypeError', () => {
        const obj1 = null;
        const obj2 = [];
        expect(() => mergeObjects(obj1, obj2)).toThrow(TypeError);
        expect(() => mergeObjects(obj2, obj1)).toThrow(TypeError);
    });
});