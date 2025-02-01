const deepMergeObjects = (obj1, obj2) => {
    if (obj2 === null || obj2 === undefined) {
        return obj1;
    }

    const result = { ...obj1 };

    for (const key in obj2) {
        if (obj2.hasOwnProperty(key)) {
            if (typeof obj2[key] === 'object' && obj2[key] !== null && !Array.isArray(obj2[key])) {
                if (!obj1.hasOwnProperty(key)) {
                    result[key] = obj2[key];
                } else {
                    result[key] = deepMergeObjects(obj1[key], obj2[key]);
                }
            } else {
                result[key] = obj2[key];
            }
        }
    }

    return result;
};
describe('deepMergeObjects', () => {
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
        expect(result).toEqual({
            a: {
                b: {
                    c: 1
                }
            },
            d: 2
        });
    });

    test('does not merge arrays but takes them from obj1', () => {
        const obj1 = { a: [1, 2, 3] };
        const obj2 = { a: [4, 5] };
        const result = deepMergeObjects(obj1, obj2);
        expect(result).toEqual({ a: [1, 2, 3] }); // Should keep array from obj1
    });
});
