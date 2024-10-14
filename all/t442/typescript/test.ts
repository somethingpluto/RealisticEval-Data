import { convertStringsToNumbers } from './path/to/convertStringsToNumbers'; // Adjust the path as needed

describe('convertStringsToNumbers', () => {
    it('should handle empty objects', () => {
        expect(convertStringsToNumbers({})).toEqual({});
    });

    it('should handle empty arrays', () => {
        expect(convertStringsToNumbers([])).toEqual([]);
    });

    it('should handle simple objects', () => {
        const input = { name: 'John', age: '30', height: '5.9' };
        const expected = { name: 'John', age: 30, height: 5.9 };
        expect(convertStringsToNumbers(input)).toEqual(expected);
    });

    it('should handle nested objects', () => {
        const input = {
            name: 'John',
            age: '30',
            height: '5.9',
            children: ['Alice', 'Bob'],
            nested: { inner: '42' }
        };
        const expected = {
            name: 'John',
            age: 30,
            height: 5.9,
            children: ['Alice', 'Bob'],
            nested: { inner: 42 }
        };
        expect(convertStringsToNumbers(input)).toEqual(expected);
    });

    it('should handle simple arrays', () => {
        const input = ['John', '30', '5.9'];
        const expected = ['John', 30, 5.9];
        expect(convertStringsToNumbers(input)).toEqual(expected);
    });

    it('should handle nested arrays', () => {
        const input = ['John', '30', '5.9', ['Alice', 'Bob'], [{ inner: '42' }]];
        const expected = ['John', 30, 5.9, ['Alice', 'Bob'], [{ inner: 42 }]];
        expect(convertStringsToNumbers(input)).toEqual(expected);
    });

    it('should handle mixed structures', () => {
        const input = {
            name: 'John',
            age: '30',
            height: '5.9',
            children: ['Alice', 'Bob'],
            nested: { inner: '42', subNested: ['sub1', 'sub2'] }
        };
        const expected = {
            name: 'John',
            age: 30,
            height: 5.9,
            children: ['Alice', 'Bob'],
            nested: { inner: 42, subNested: ['sub1', 'sub2'] }
        };
        expect(convertStringsToNumbers(input)).toEqual(expected);
    });

    it('should handle non-string data', () => {
        const input = {
            name: 'John',
            age: 30,
            height: 5.9,
            children: ['Alice', 'Bob'],
            nested: { inner: 42, subNested: ['sub1', 'sub2'] }
        };
        expect(convertStringsToNumbers(input)).toEqual(input);
    });
});
