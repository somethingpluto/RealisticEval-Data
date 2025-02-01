/**
 * Find and return an array of all placeholders in the format {{ placeholder }} from the input text.
 *
 * @param {string} text - The input string containing potential placeholders.
 * @returns {Array} An array of matching placeholders.
 */
function findPlaceholders(text) {
    const regex = /\{\{(\w+)\}\}/g;
    const matches = [];
    let match;

    while ((match = regex.exec(text)) !== null) {
        matches.push(match[0]);
    }

    return matches;
}
describe('TestFindPlaceholders', () => {
  it('test string with multiple placeholders', () => {
      const inputText = "Here are some placeholders: {{ placeholder1 }}, {{ placeholder2 }}, and {{ placeholder3 }}.";
      const expectedOutput = ['placeholder1', 'placeholder2', 'placeholder3'];
      expect(findPlaceholders(inputText)).toEqual(expectedOutput);
  });

  it('test string with no placeholders', () => {
      const inputText = "This string has no placeholders.";
      const expectedOutput = [];
      expect(findPlaceholders(inputText)).toEqual(expectedOutput);
  });

  it('test string with a single placeholder', () => {
      const inputText = "The only placeholder is {{ singlePlaceholder }}.";
      const expectedOutput = ['singlePlaceholder'];
      expect(findPlaceholders(inputText)).toEqual(expectedOutput);
  });

  it('test string with placeholders that have extra spaces', () => {
      const inputText = "Placeholders with spaces: {{  placeholder_with_spaces  }} and {{ placeholder2 }}.";
      const expectedOutput = ['placeholder_with_spaces', 'placeholder2'];
      expect(findPlaceholders(inputText)).toEqual(expectedOutput);
  });
});
