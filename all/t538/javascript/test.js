describe('sortAlphabetically', () => {
    const data = [
        { name: 'banana' },
        { name: 'Apple' },
        { name: 'cherry' },
        { name: 'apple' },
        { name: 'Banana' },
        { name: 'date' }
    ];

    test('sorts an array of strings in ascending order', () => {
        const result = sortAlphabetically(data, item => item.name);
        expect(result).toEqual([
            { name: 'Apple' },
            { name: 'Banana' },
            { name: 'apple' },
            { name: 'banana' },
            { name: 'cherry' },
            { name: 'date' }
        ]);
    });

    test('sorts an array of strings in descending order', () => {
        const result = sortAlphabetically(data, item => item.name, false);
        expect(result).toEqual([
            { name: 'date' },
            { name: 'cherry' },
            { name: 'banana' },
            { name: 'apple' },
            { name: 'Banana' },
            { name: 'Apple' }
        ]);
    });

    test('handles an empty array', () => {
        const result = sortAlphabetically([], item => item.name);
        expect(result).toEqual([]);
    });

    test('sorts when all items are the same', () => {
        const sameData = [{ name: 'apple' }, { name: 'apple' }];
        const result = sortAlphabetically(sameData, item => item.name);
        expect(result).toEqual(sameData);
    });

    test('correctly sorts with mixed case', () => {
        const mixedCaseData = [
            { name: 'apple' },
            { name: 'banana' },
            { name: 'Apple' },
            { name: 'Banana' }
        ];
        const result = sortAlphabetically(mixedCaseData, item => item.name);
        expect(result).toEqual([
            { name: 'Apple' },
            { name: 'Banana' },
            { name: 'apple' },
            { name: 'banana' }
        ]);
    });

    test('sorts strings with special characters', () => {
        const specialCharData = [
            { name: 'banana' },
            { name: 'apple!' },
            { name: '#apple' },
            { name: 'cherry' }
        ];
        const result = sortAlphabetically(specialCharData, item => item.name);
        expect(result).toEqual([
            { name: '#apple' },
            { name: 'apple!' },
            { name: 'banana' },
            { name: 'cherry' }
        ]);
    });

    test('sorts strings with numeric characters', () => {
        const numericData = [
            { name: 'apple2' },
            { name: 'apple10' },
            { name: 'apple1' }
        ];
        const result = sortAlphabetically(numericData, item => item.name);
        expect(result).toEqual([
            { name: 'apple1' },
            { name: 'apple10' },
            { name: 'apple2' }
        ]);
    });

    test('sorts an array of strings in ascending order with numbers', () => {
        const numericData = [
            { name: 'Banana' },
            { name: '2Banana' },
            { name: '1Banana' },
            { name: 'Apple' }
        ];
        const result = sortAlphabetically(numericData, item => item.name);
        expect(result).toEqual([
            { name: '1Banana' },
            { name: '2Banana' },
            { name: 'Apple' },
            { name: 'Banana' }
        ]);
    });
});