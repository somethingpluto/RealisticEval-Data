// ... (previous code for context)
function convertCsvValues(row: Record<string, string>): Record<string, string | null> {
    const result: Record<string, string | null> = {};
    const numericRegex = /^[+-]?\d*\.?\d+$/;

    for (const [key, value] of Object.entries(row)) {
        if (numericRegex.test(value)) {
            result[key] = value.replace(/,/g, '.');
        } else {
            result[key] = null;
        }
    }

    return result;
}

// Unit tests
describe('convertCsvValues', () => {
    it('converts numeric strings with commas to dots', () => {
        const input = { "price": "1,234.56" };
        const expected = { "price": "1.234,56" };
        expect(convertCsvValues(input)).toEqual(expected);
    });

    it('converts numeric strings without commas to themselves', () => {
        const input = { "price": "1234.56" };
        const expected = { "price": "1234.56" };
        expect(convertCsvValues(input)).toEqual(expected);
    });

    it('sets non-numeric strings to null', () => {
        const input = { "price": "not a number" };
        const expected = { "price": null };
        expect(convertCsvValues(input)).toEqual(expected);
    });
});
// ... (rest of the code)
describe('TestConvertCsvValues', () => {
    describe('testValidNumericStrings', () => {
        it('should handle valid numeric strings including commas', () => {
            const row = { value1: '1,234', value2: '5,678', value3: '9,876' };
            const expected = { value1: '1.234', value2: '5.678', value3: '9.876' };
            const result = convertCsvValues(row);
            expect(result).toEqual(expected);
        });
    });

    describe('testNonNumericStrings', () => {
        it('should handle non-numeric strings', () => {
            const row = { value1: 'not_a_number', value2: 'hello', value3: 'world' };
            const expected = { value1: null, value2: null, value3: null };
            const result = convertCsvValues(row);
            expect(result).toEqual(expected);
        });
    });

    describe('testMixedValues', () => {
        it('should handle a mix of numeric and non-numeric strings', () => {
            const row = { value1: '1,234', value2: 'not_a_number', value3: '3,14159' };
            const expected = { value1: '1.234', value2: null, value3: '3.14159' };
            const result = convertCsvValues(row);
            expect(result).toEqual(expected);
        });
    });

    describe('testNoValues', () => {
        it('should handle a mix of non-numeric and numeric strings', () => {
            const row = { value1: 'aaaa', value2: 'not_a_number', value3: '3,14' };
            const expected = { value1: null, value2: null, value3: '3.14' };
            const result = convertCsvValues(row);
            expect(result).toEqual(expected);
        });
    });

    describe('testEdgeCases', () => {
        it('should handle edge cases with empty strings and negative numbers', () => {
            const row = { value1: '', value2: '0.0', value3: '1,23' };
            const expected = { value1: null, value2: '0.0', value3: '1.23' };
            const result = convertCsvValues(row);
            expect(result).toEqual(expected);
        });
    });
});
