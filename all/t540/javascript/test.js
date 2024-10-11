describe('generateUniquePairs', () => {
    test('generates unique pairs from an array with three elements', () => {
        const items = ['A', 'B', 'C'];
        const result = generateUniquePairs(items);
        expect(result).toEqual([
            ['A', 'B'],
            ['A', 'C'],
            ['B', 'C']
        ]);
    });

    test('generates unique pairs from an array with two elements', () => {
        const items = ['A', 'B'];
        const result = generateUniquePairs(items);
        expect(result).toEqual([['A', 'B']]);
    });

    test('returns an empty array when the input array is empty', () => {
        const items = [];
        const result = generateUniquePairs(items);
        expect(result).toEqual([]);
    });

    test('returns an empty array when the input array has one element', () => {
        const items = ['A'];
        const result = generateUniquePairs(items);
        expect(result).toEqual([]);
    });


    test('handles an array with different types of elements', () => {
        const items = [1, 'A', { key: 'value' }];
        const result = generateUniquePairs(items);
        expect(result).toEqual([
            [1, 'A'],
            [1, { key: 'value' }],
            ['A', { key: 'value' }]
        ]);
    });

    test('generates pairs from an array with more than three elements', () => {
        const items = ['A', 'B', 'C', 'D'];
        const result = generateUniquePairs(items);
        expect(result).toEqual([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['B', 'C'],
            ['B', 'D'],
            ['C', 'D']
        ]);
    });

});
