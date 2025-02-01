/**
 * Cleans the input object by removing keys with invalid values. Valid values are non-NaN, non-null, and non-whitespace strings.
 *
 * @param {Object} inputDict - An object to be cleaned.
 * @returns {Object} A new object containing only valid values.
 */
function cleanDictionary(inputDict) {
    const cleanedDict = {};
    for (const key in inputDict) {
        if (inputDict.hasOwnProperty(key)) {
            const value = inputDict[key];
            if (typeof value === 'string' && value.trim() !== '') {
                cleanedDict[key] = value;
            } else if (typeof value !== 'string' && !isNaN(value) && value !== null) {
                cleanedDict[key] = value;
            }
        }
    }
    return cleanedDict;
}
describe('TestCleanDictionary', () => {
    describe('testValidStrings', () => {
        it('should handle a dictionary with valid strings', () => {
            const inputDict = {
                'key1': 'valid string',
                'key2': 'another valid string'
            };
            const expectedOutput = {
                'key1': 'valid string',
                'key2': 'another valid string'
            };
            expect(cleanDictionary(inputDict)).toEqual(expectedOutput);
        });
    });

    describe('testNoneAndNaNValues', () => {
        it('should handle a dictionary with None and NaN values', () => {
            const inputDict = {
                'key1': null,
                'key3': 'valid string'
            };
            const expectedOutput = {
                'key3': 'valid string'
            };
            expect(cleanDictionary(inputDict)).toEqual(expectedOutput);
        });
    });

    describe('testWhitespaceStrings', () => {
        it('should handle a dictionary with whitespace strings', () => {
            const inputDict = {
                'key1': '   ',
                'key2': '',
                'key3': 'valid'
            };
            const expectedOutput = {
                'key3': 'valid'
            };
            expect(cleanDictionary(inputDict)).toEqual(expectedOutput);
        });
    });

    describe('testEmptyDictionary', () => {
        it('should handle an empty dictionary', () => {
            const inputDict = {};
            const expectedOutput = {};
            expect(cleanDictionary(inputDict)).toEqual(expectedOutput);
        });
    });
});
