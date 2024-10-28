const { DataFrame } = require('dataframe-js');
describe('TestFillMissingWithFirstValid', () => {
    describe('test_basic_filling', () => {
        it('fills missing values correctly', () => {
            const df = new DataFrame({
                A: [1, null, 3, null],
                B: ['foo', 'bar', null, 'baz']
            });
            const result = fillMissingWithFirstValid(df, 'B');
            const expected = new DataFrame({
                A: [1, null, 3, null],
                B: ['foo', 'bar', 'foo', 'baz']
            });

            expect(result.equals(expected)).toBe(true);
        });
    });

    describe('test_no_missing_values', () => {
        it('does not change the DataFrame when no missing values', () => {
            const df = new DataFrame({
                A: [1, 2, 3],
                B: ['foo', 'bar', 'baz']
            });
            const result = fillMissingWithFirstValid(df, 'B');
            const expected = new DataFrame({
                A: [1, 2, 3],
                B: ['foo', 'bar', 'baz']
            });

            expect(result.equals(expected)).toBe(true);
        });
    });

    describe('test_single_valid_value', () => {
        it('fills all missing values with the single valid value', () => {
            const df = new DataFrame({
                A: [1, null, null, 4],
                B: [null, 'bar', null, null]
            });
            const result = fillMissingWithFirstValid(df, 'B');
            const expected = new DataFrame({
                A: [1, null, null, 4],
                B: ['bar', 'bar', 'bar', 'bar']
            });

            expect(result.equals(expected)).toBe(true);
        });
    });

    describe('test_multiple_valid_values', () => {
        it('fills missing values with the first valid value', () => {
            const df = new DataFrame({
                A: [1, null, 3, 4],
                B: [null, 'bar', 'foo', null]
            });
            const result = fillMissingWithFirstValid(df, 'B');
            const expected = new DataFrame({
                A: [1, null, 3, 4],
                B: ['bar', 'bar', 'foo', 'bar']
            });

            expect(result.equals(expected)).toBe(true);
        });
    });
});