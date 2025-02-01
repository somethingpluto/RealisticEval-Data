/**
 * Converts a camelCase string to a format with the first letter capitalized and spaces between words.
 * For example:
 *      input: "thisIsTest"
 *      output: "This is test"
 *
 * @param {string} input The camelCase string to be converted.
 * @returns {string} The converted string with spaces and initial capitalization.
 */
function camelCaseToCapitalizedWithSpaces(input) {
    if (typeof input !== 'string') {
        throw new Error('Input must be a string');
    }

    let result = '';
    for (let i = 0; i < input.length; i++) {
        if (i === 0) {
            result += input[i].toUpperCase();
        } else if (input[i] === input[i].toUpperCase() && input[i] !== input[i].toLowerCase()) {
            result += ' ' + input[i].toUpperCase();
        } else {
            result += input[i];
        }
    }
    return result;
}
describe('convertCamelCaseToSentence', () => {
    test('should convert a simple camelCase string to a sentence', () => {
        const input = "thisIsTest";
        const expectedOutput = "This is test";
        expect(camelCaseToCapitalizedWithSpaces(input)).toBe(expectedOutput);
    });

    test('should handle single word starting with lowercase', () => {
        const input = "example";
        const expectedOutput = "Example";
        expect(camelCaseToCapitalizedWithSpaces(input)).toBe(expectedOutput);
    });

    test('should handle a camelCase string with multiple uppercase letters', () => {
        const input = "thisIsAnExampleString";
        const expectedOutput = "This is an example string";
        expect(camelCaseToCapitalizedWithSpaces(input)).toBe(expectedOutput);
    });

    test('should handle a single uppercase letter', () => {
        const input = "aSingleUppercaseLetterX";
        const expectedOutput = "A single uppercase letter x";
        expect(camelCaseToCapitalizedWithSpaces(input)).toBe(expectedOutput);
    });

    test('should handle an already capitalized string', () => {
        const input = "AlreadyCapitalized";
        const expectedOutput = "Already capitalized";
        expect(camelCaseToCapitalizedWithSpaces(input)).toBe(expectedOutput);
    });
});
