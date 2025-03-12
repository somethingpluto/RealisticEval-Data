import { wrap } from 'textwrap';
import { execSync } from 'child_process';

function* wrapContentGenerator(content: string, width: number = 80): Generator<string> {
  const wrappedLines = wrap(content, { width });
  for (const line of wrappedLines) {
    yield line;
  }
}

function processLinesWithPython(lines: string[]): void {
  const pythonScript = `
import sys
lines = [line.strip() for line in sys.stdin if line.strip()]
print('\n'.join(lines))
  `;
  const process = execSync(`python -c "${pythonScript}"`, { input: lines.join('\n') });
  console.log(process.toString());
}

// Usage example:
// const lines = [...wrapContentGenerator(yourContent)];
// processLinesWithPython(lines);
describe('wrapContentGenerator', () => {
  it('should handle empty content', () => {
    const result = Array.from(wrapContentGenerator(""));
    expect(result).toEqual([]);
  });

  it('should handle a single line of content within default width', () => {
    const result = Array.from(wrapContentGenerator("Hello, world!"));
    expect(result).toEqual(["Hello, world!"]);
  });

  it('should handle multiple lines of content each fitting within default width', () => {
    const content = "Hello\nWorld\nPython";
    const result = Array.from(wrapContentGenerator(content));
    expect(result).toEqual(["Hello", "World", "Python"]);
  });

  it('should handle a single long line that exceeds the default width', () => {
    const content = "This is a very long line that should definitely be wrapped around the default width of 80 characters.";
    const result = Array.from(wrapContentGenerator(content));
    const longestLine = result.reduce((max, line) => line.length > max.length ? line : max, "");
    expect(longestLine.length).toBeLessThanOrEqual(80);
  });

  it('should handle a custom width', () => {
    const content = "This is a test for custom width setting.";
    const result = Array.from(wrapContentGenerator(content, 10));
    expect(result.every(line => line.length <= 10)).toBe(true);
  });

  it('should handle content that contains only whitespace characters', () => {
    const result = Array.from(wrapContentGenerator("     "));
    expect(result).toEqual(["\n"]);
  });
});
