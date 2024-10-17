describe('TestConvertCsvValues', () => {
    describe('test_valid_numeric_strings', () => {
        it('should handle valid numeric strings including commas', () => {
            const row = {'value1': '1,234', 'value2': '5,678', 'value3': '9,876'};
            const expected = {'value1': '1.234', 'value2': '5.678', 'value3': '9.876'};
            const result = convertCsvValues(row);
            expect(result).toEqual(expected);
        });
    });

    describe('test_non_numeric_strings', () => {
        it('should handle non-numeric strings', () => {
            const row = {'value1': 'not_a_number', 'value2': 'hello', 'value3': 'world'};
            const expected = {'value1': null, 'value2': null, 'value3': null};
            const result = convertCsvValues(row);
            expect(result).toEqual(expected);
        });
    });

    describe('test_mixed_values', () => {
        it('should handle a mix of numeric and non-numeric strings', () => {
            const row = {'value1': '1,234', 'value2': 'not_a_number', 'value3': '3,14159'};
            const expected = {'value1': '1.234', 'value2': null, 'value3': '3.14159'};
            const result = convertCsvValues(row);
            expect(result).toEqual(expected);
        });
    });

    describe('test_no_values', () => {
        it('should handle a mix of non-numeric and numeric strings', () => {
            const row = {'value1': 'aaaa', 'value2': 'not_a_number', 'value3': '3,14'};
            const expected = {'value1': null, 'value2': null, 'value3': '3.14'};
            const result = convertCsvValues(row);
            expect(result).toEqual(expected);
        });
    });

    describe('test_edge_cases', () => {
        it('should handle edge cases with empty strings and negative numbers', () => {
            const row = {'value1': '', 'value2': '0.0', 'value3': '1,23'};
            const expected = {'value1': null, 'value2': '0.0', 'value3': '1.23'};
            const result = convertCsvValues(row);
            expect(result).toEqual(expected);
        });
    });
});