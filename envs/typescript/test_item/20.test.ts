import { execSync } from 'child_process';

function removeInnerAsterisks(text: string): string {
  // ... (previous code remains unchanged)

  // New functionality to call Python script
  const sanitizedText = text.replace(/\*/g, '');
  const pythonScriptPath = 'path_to_your_script.py';
  try {
    const result = execSync(`python ${pythonScriptPath} "${sanitizedText}"`);
    return result.toString();
  } catch (error) {
    console.error('Error calling Python script:', error);
    return sanitizedText;
  }
}
describe('removeInnerAsterisks', () => {
    test('basic case', () => {
        const text = "Hello (*wo*rld*)!";
        const expected = "Hello (*world*)!";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('multiple asterisks', () => {
        const text = "(*he*l*lo*)";
        const expected = "(*hello*)";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('no asterisks inside', () => {
        const text = "(*hello*)";
        const expected = "(*hello*)";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('multiple patterns', () => {
        const text = "(*hi*), (*there*), (*world*)!";
        const expected = "(*hi*), (*there*), (*world*)!";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('no matching pattern', () => {
        const text = "This is a test without matching parentheses.";
        const expected = "This is a test without matching parentheses.";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });
});

