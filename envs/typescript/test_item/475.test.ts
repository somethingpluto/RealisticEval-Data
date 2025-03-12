// Additions at the start of the file
import { escapeRegExp } from 'lodash';

// Changes within the function
function safeFormat(template: string, ...kwargs: [string, any][]): string {
  const escapedTemplate = template.replace(/{(\w+)}/g, (match, key) => {
    const escapedKey = escapeRegExp(key);
    return kwargs.find(([k]) => k === escapedKey) ? kwargs.find(([k]) => k === escapedKey)[1] : match;
  });
  return escapedTemplate;
}
// Rest of the file remains unchanged
describe('TestSafeFormat', () => {
    it('test_full_replacement', () => {
        // Test with all placeholders having corresponding values.
        const template = "Hello, {name}! Welcome to {place}.";
        const result = safeFormat(template, ['name', 'Alice'], ['place', 'Wonderland']);
        const expected = "Hello, Alice! Welcome to Wonderland.";
        expect(result).toEqual(expected);
    });

    it('test_partial_replacement', () => {
        // Test with some placeholders missing corresponding values.
        const template = "Hello, {name}! Welcome to {place}.";
        const result = safeFormat(template, ['name', 'Alice']);
        const expected = "Hello, Alice! Welcome to {place}.";
        expect(result).toEqual(expected);
    });

    it('test_no_replacement', () => {
        // Test when no placeholders are provided.
        const template = "Hello, world!";
        const result = safeFormat(template);
        const expected = "Hello, world!";
        expect(result).toEqual(expected);
    });

    it('test_missing_placeholder', () => {
        // Test with a placeholder that has no corresponding value.
        const template = "My name is {name}, and I live in {city}.";
        const result = safeFormat(template, ['name', 'Alice']);
        const expected = "My name is Alice, and I live in {city}.";
        expect(result).toEqual(expected);
    });

    it('test_numeric_values', () => {
        // Test with numeric values as replacements.
        const template = "Your score is {score} out of {total}.";
        const result = safeFormat(template, ['score', 85], ['total', 100]);
        const expected = "Your score is 85 out of 100.";
        expect(result).toEqual(expected);
    });
});
