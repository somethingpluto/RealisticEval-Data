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