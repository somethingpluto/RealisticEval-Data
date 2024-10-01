describe('deepMergeObjects', () => {
    test('merges two flat objects', () => {
        const obj1 = { a: 1, b: 2 };
        const obj2 = { b: 3, c: 4 };
        const result = deepMergeObjects(obj1, obj2);
        expect(result).toEqual({ a: 1, b: 2, c: 4 }); // obj1 value should take precedence
    });


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
        expect(result).toEqual({ a: { b: { c: 1, d: 3 } }, d: 2, e: 4 });
    });

    test('preserves non-object values in obj1 when keys collide', () => {
        const obj1 = { a: 1, b: { x: 5 }, c: 3 };
        const obj2 = { b: { x: 10, y: 20 }, c: 4 };
        const result = deepMergeObjects(obj1, obj2);
        expect(result).toEqual({ a: 1, b: { x: 5, y: 20 }, c: 3 }); // c from obj1 should be preserved
    });
});