import * as re from 'xregexp';

/**
 * Find and return a list of all placeholders in the format {{ placeholder }} from the input text.
 *
 * @param text - The input string containing potential placeholders.
 * @returns An array of matching placeholders.
 */
function findPlaceholders(text: string): string[] {
  const regex = re.XRegExp('\\{\\{[\\s\\S]*?\\}\\}\\s*');
  const matches = re.match(text, regex);
  return matches ? matches : [];
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
