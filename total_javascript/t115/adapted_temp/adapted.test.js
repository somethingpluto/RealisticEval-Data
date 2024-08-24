describe('sortObjectsByKey', () => {
    const items = [
        {name: 'apple', id: 2},
        {name: 'Orange', id: 1},
        {name: 'banana', id: 3}
    ];

    test('correctly sorts an array of objects by a string key case-insensitively', () => {
        const sorted = sortObjectsByKey(items, 'name');
        expect(sorted).toEqual([
            {name: 'apple', id: 2},
            {name: 'banana', id: 3},
            {name: 'Orange', id: 1}
        ]);
    });

    test('throws an error when the key does not exist on one or more objects', () => {
        expect(() => sortObjectsByKey(items, 'color')).toThrow(/does not exist/);
    });

    test('throws an error if the first argument is not an array', () => {
        expect(() => sortObjectsByKey('not-an-array', 'name')).toThrow(TypeError);
    });

    test('throws an error if the array is empty', () => {
        expect(() => sortObjectsByKey([], 'name')).toThrow(/should not be empty/);
    });

    test('throws an error if the key is not a string', () => {
        expect(() => sortObjectsByKey(items, 123)).toThrow(TypeError);
    });
});

function sortObjectsByKey(array, key) {
    if (!Array.isArray(array)) {
        throw new TypeError("The first argument must be an array.");
    }
    if (typeof key !== 'string') {
        throw new TypeError("The key must be a string.");
    }
    if (array.length === 0) {
        throw new Error("The array should not be empty.");
    }
    if (!array.every(obj => obj.hasOwnProperty(key))) {
        throw new Error(`The key "${key}" does not exist in one or more objects.`);
    }

    return array.slice().sort((a, b) => {
        const valueA = String(a[key]).toLowerCase(); // Convert to string to handle non-string fields
        const valueB = String(b[key]).toLowerCase();

        return valueA.localeCompare(valueB);
    });
}