// Start of the code context
import { toTitleCase } from 'lodash';

function camelCaseToCapitalizedWithSpaces(input: string): string {
    const words = input.split(/(?=[A-Z])/);
    const capitalizedWords = words.map(word => toTitleCase(word));
    return capitalizedWords.join(' ');
}
// End of the code context
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
