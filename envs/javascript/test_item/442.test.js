/**
 * Convert strings in nested structures (e.g., dictionaries, arrays) to numbers (integers or floating-point numbers) as much as possible.
 *
 * @param {Object|Array} data - The input data before conversion.
 * @returns {Object|Array} - The converted data.
 */
function convertStringsToNumbers(data) {
    if (typeof data === 'string') {
        // Attempt to convert the string to a number
        const num = Number(data);
        return isNaN(num) ? data : num;
    } else if (Array.isArray(data)) {
        // Recursively process each element in the array
        return data.map(convertStringsToNumbers);
    } else if (typeof data === 'object' && data !== null) {
        // Recursively process each property in the object
        const result = {};
        for (const key in data) {
            if (data.hasOwnProperty(key)) {
                result[key] = convertStringsToNumbers(data[key]);
            }
        }
        return result;
    }
    // Return the data as-is if it's not a string, array, or object
    return data;
}
describe('TestConvertStringsToNumbers', () => {
    describe('test_flat_dict', () => {
        it('should correctly convert flat dictionary', () => {
            const data = {'a': '1', 'b': '2.5', 'c': 'not a number'};
            const expected = {'a': 1, 'b': 2.5, 'c': 'not a number'};
            expect(convertStringsToNumbers(data)).toEqual(expected);
        });
    });

    describe('test_nested_dict', () => {
        it('should correctly convert nested dictionary', () => {
            const data = {'x': {'y': '10', 'z': '3.14'}, 'w': '20.0'};
            const expected = {'x': {'y': 10, 'z': 3.14}, 'w': 20.0};
            expect(convertStringsToNumbers(data)).toEqual(expected);
        });
    });

    describe('test_list_of_strings', () => {
        it('should correctly convert list of strings', () => {
            const data = ['1', '2.5', '3', 'invalid'];
            const expected = [1, 2.5, 3, 'invalid'];
            expect(convertStringsToNumbers(data)).toEqual(expected);
        });
    });

    describe('test_mixed_structure', () => {
        it('should correctly convert mixed structure', () => {
            const data = {'numbers': ['1', '2.0', 3], 'more_numbers': [{'num': '4'}, '5']};
            const expected = {'numbers': [1, 2.0, 3], 'more_numbers': [{'num': 4}, 5]};
            expect(convertStringsToNumbers(data)).toEqual(expected);
        });
    });

    describe('test_empty_structure', () => {
        it('should correctly handle empty structure', () => {
            const data = {};
            const expected = {};
            expect(convertStringsToNumbers(data)).toEqual(expected);
        });
    });
});
