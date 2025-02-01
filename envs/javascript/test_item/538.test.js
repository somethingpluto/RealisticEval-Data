/**
 * Sorts an array of objects alphabetically based on a specified field.
 *
 * @param {Array} array - The array of objects to sort.
 * @param {String} field - The field of the objects to sort by.
 * @param {Boolean} ascending - If true, sort in ascending order; if false, sort in descending order.
 * @returns {Array} - The sorted array of objects.
 */
function sortByField(array, field, ascending = true) {
    return array.sort((a, b) => {
        if (a[field] < b[field]) {
            return ascending ? -1 : 1;
        }
        if (a[field] > b[field]) {
            return ascending ? 1 : -1;
        }
        return 0;
    });
}
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
