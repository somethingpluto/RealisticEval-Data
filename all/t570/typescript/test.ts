describe('deepMergeObjects', () => {


    test('handles null values in obj2', () => {
        const obj1 = {a: 1, b: 2};
        const obj2 = null;
        const result = deepMergeObjects(obj1, obj2);
        expect(result).toEqual(obj1); // Should return obj1
    });

    test('handles undefined values in obj2', () => {
        const obj1 = {a: 1, b: 2};
        const obj2 = undefined;
        const result = deepMergeObjects(obj1, obj2);
        expect(result).toEqual(obj1); // Should return obj1
    });

    test('merges deeply nested objects', () => {
        const obj1 = {a: {b: {c: 1}}, d: 2};
        const obj2 = {a: {b: {d: 3}}, e: 4};
        const result = deepMergeObjects(obj1, obj2);
        expect(result).toEqual({
            "a": {
                "b": {
                    "c": 1
                }
            },
            "d": 2
        });
    });

    test('does not merge arrays but takes them from obj1', () => {
    const obj1 = {a: [1, 2, 3]};
    const obj2 = {a: [4, 5]};
    const result = deepMergeObjects(obj1, obj2);
    expect(result).toEqual({a: [1, 2, 3]}); // Should keep array from obj1
});
});