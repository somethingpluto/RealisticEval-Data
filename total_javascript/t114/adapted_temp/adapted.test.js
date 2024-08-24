describe('sortByTimestamp', () => {
    // Test data setup
    const items = [
        {id: 1, date: '2021-01-01'},
        {id: 2, date: '2020-01-01'},
        {id: 3, date: '2022-01-01'}
    ];

    const getField = item => item.date;

    test('sorts array of objects in ascending order by default', () => {
        const expected = [items[1], items[0], items[2]]; // Sorted by date
        expect(sortByTimestamp(items, getField)).toEqual(expected);
    });

    test('sorts array of objects in descending order when specified', () => {
        const expected = [items[2], items[0], items[1]]; // Sorted by date descending
        expect(sortByTimestamp(items, getField, false)).toEqual(expected);
    });

    test('handles invalid date formats by pushing them to the end', () => {
        const invalidItems = [
            {id: 1, date: '2021-01-01'},
            {id: 2, date: 'not-a-date'},
            {id: 3, date: '2020-01-01'}
        ];
        const expected = [invalidItems[2], invalidItems[0], invalidItems[1]]; // Invalid dates last
        expect(sortByTimestamp(invalidItems, getField)).toEqual(expected);
    });

    test('throws an error when the first argument is not an array', () => {
        const input = 'not-an-array';
        expect(() => sortByTimestamp(input, getField)).toThrow('The first argument must be an array.');
    });

    test('returns an empty array when provided an empty array', () => {
        expect(sortByTimestamp([], getField)).toEqual([]);
    });
});

/**
 * Sorts an array of objects based on timestamp values extracted by a getter function.
 * @param {Object[]} arr - The array of objects to sort.
 * @param {function} getField - A function that takes an object and returns its timestamp.
 * @param {boolean} ascending - True for ascending order, false for descending. Defaults to true.
 * @returns {Object[]} The sorted array.
 */
function sortByTimestamp(arr, getField, ascending = true) {
    if (!Array.isArray(arr)) {
        throw new Error("The first argument must be an array.");
    }

    const sortedArr = arr.slice().sort((a, b) => {
        // Extract timestamps using the getField callback
        const dateA = new Date(getField(a));
        const dateB = new Date(getField(b));

        // Compare the timestamp values
        const timeA = dateA.getTime();
        const timeB = dateB.getTime();

        // Handle potentially invalid dates by treating them as less than valid dates
        if (isNaN(timeA)) return 1; // Push invalid dates to the end
        if (isNaN(timeB)) return -1; // Push invalid dates to the end

        // Determine sort order based on the 'ascending' flag
        return ascending ? timeA - timeB : timeB - timeA;
    });

    return sortedArr;
}