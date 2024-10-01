describe('sortByField', () => {
    const data = [
        {name: 'John', age: 25},
        {name: 'Alice', age: 30},
        {name: 'Bob', age: 22},
        {name: 'Charlie', age: 28},
    ];

    test('should sort by name in ascending order', () => {
        const sorted = sortByField(data, 'name', true);
        expect(sorted).toEqual([
            {name: 'Alice', age: 30},
            {name: 'Bob', age: 22},
            {name: 'Charlie', age: 28},
            {name: 'John', age: 25},
        ]);
    });

    test('should sort by name in descending order', () => {
        const sorted = sortByField(data, 'name', false);
        expect(sorted).toEqual([
            {name: 'John', age: 25},
            {name: 'Charlie', age: 28},
            {name: 'Bob', age: 22},
            {name: 'Alice', age: 30},
        ]);
    });

    test('should sort by age in ascending order', () => {
        const sorted = sortByField(data, 'age', true);
        expect(sorted).toEqual([
            {name: 'Bob', age: 22},
            {name: 'John', age: 25},
            {name: 'Charlie', age: 28},
            {name: 'Alice', age: 30},
        ]);
    });

    test('should sort by age in descending order', () => {
        const sorted = sortByField(data, 'age', false);
        expect(sorted).toEqual([
            {name: 'Alice', age: 30},
            {name: 'Charlie', age: 28},
            {name: 'John', age: 25},
            {name: 'Bob', age: 22},
        ]);
    });
});