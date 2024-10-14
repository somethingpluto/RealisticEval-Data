describe('convertStringsToNumbers', () => {
    it('should handle empty objects and arrays', () => {
        expect(convertStringsToNumbers({})).toEqual({});
        expect(convertStringsToNumbers([])).toEqual([]);
    });

    it('should handle nested objects and arrays', () => {
        const nestedData = {
            a: '1',
            b: ['2', '3'],
            c: {
                d: '4',
                e: '5.5'
            }
        };
        const expectedResult = {
            a: 1,
            b: [2, 3],
            c: {
                d: 4,
                e: 5.5
            }
        };
        expect(convertStringsToNumbers(nestedData)).toEqual(expectedResult);
    });

    it('should handle mixed types', () => {
        const mixedData = {
            a: 'hello',
            b: ['1', '2.5', 'three'],
            c: {
                d: '4',
                e: '5.5',
                f: true
            }
        };
        const expectedResult = {
            a: 'hello',
            b: [1, 2.5, 'three'],
            c: {
                d: 4,
                e: 5.5,
                f: true
            }
        };
        expect(convertStringsToNumbers(mixedData)).toEqual(expectedResult);
    });

    it('should handle deeply nested structures', () => {
        const deepData = {
            a: '1',
            b: [
                '2',
                { c: '3', d: ['4', '5.5'] },
                [6, '7.7']
            ]
        };
        const expectedResult = {
            a: 1,
            b: [
                2,
                { c: 3, d: [4, 5.5] },
                [6, 7.7]
            ]
        };
        expect(convertStringsToNumbers(deepData)).toEqual(expectedResult);
    });

    it('should handle non-string values', () => {
        const nonStringData = {
            a: 1,
            b: [2, 3],
            c: {
                d: 4,
                e: 5.5
            }
        };
        expect(convertStringsToNumbers(nonStringData)).toEqual(nonStringData);
    });
});
