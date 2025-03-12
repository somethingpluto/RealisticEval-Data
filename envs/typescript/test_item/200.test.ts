import { v4 as uuidv4 } from 'uuid';

function extractStringFromBraces(input: string): string {
  const regex = /{([^}]+)}/;
  const match = input.match(regex);

  if (!match) {
    throw new Error(`No matching braces found in the input string: ${input}`);
  }

  return match[1];
}

// Unit tests
describe('extractStringFromBraces', () => {
  it('should extract the string within the first pair of braces', () => {
    expect(extractStringFromBraces('Hello {world}!')).toBe('world');
  });

  it('should throw an error if no braces are found', () => {
    expect(() => extractStringFromBraces('No braces here')).toThrow(
      'No matching braces found in the input string: No braces here'
    );
  });

  it('should throw an error if there is an odd number of braces', () => {
    expect(() => extractStringFromBraces('Hello {world}')).toThrow(
      'No matching braces found in the input string: Hello {world}'
    );
  });
});
describe("Test cases for extractStringFromBraces function", () => {
    
    test("Basic extraction", () => {
        const input = "This is a sample text with some data {data: \"value\"} and more text.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("{data: \"value\"}");
    });

    test("No braces", () => {
        const input = "This string has no braces.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("No opening brace found.");
    });

    test("Only opening brace", () => {
        const input = "This string has an opening brace { but no closing brace.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("No closing brace found.");
    });

    test("Only closing brace", () => {
        const input = "This string has a closing brace } but no opening brace.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("No opening brace found.");
    });

    test("Multiple braces", () => {
        const input = "First {first} and second {second} braces.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("{first}");
    });

    test("Empty braces", () => {
        const input = "This string has empty braces {} and some text.";
        const result = extractStringFromBraces(input);
        expect(result).toBe("{}");
    });

});
