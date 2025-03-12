// ... (previous code for context)
function formatComment(string: string, maxLength: number = 60): string {
  const lines = string.split(/[\r\n]+/).filter(Boolean);
  const formattedLines = lines.map(line => {
    const words = line.split(' ');
    let currentLine = '';
    const formattedLine = words.reduce((acc, word) => {
      if (currentLine.length + word.length + 1 <= maxLength) {
        currentLine += (acc ? ' ' : '') + word;
      } else {
        acc.push(currentLine);
        currentLine = word;
      }
      return acc;
    }, [] as string[]);
    return formattedLine.join(' ');
  });
  return '# ' + formattedLines.join('\n# ');
}
// ... (continuation of the code)
describe('TestFormatComment', () => {
    it('test with a short string that fits within max_length', () => {
        const inputString = "This is a test.";
        const expectedOutput = "# This is a test.";
        expect(formatComment(inputString)).toBe(expectedOutput);
    });

    it('test with a longer string that exceeds max_length', () => {
        const inputString = "This is a test of the format_comment function which should wrap long lines correctly.";
        const expectedOutput = 
            "# This is a test of the format_comment function which should\n" +
            "# wrap long lines correctly.";
        expect(formatComment(inputString, 60)).toBe(expectedOutput);
    });

    it('test with multiple lines of input', () => {
        const inputString = "First line.\nSecond line that is quite long and needs to be wrapped.";
        const expectedOutput = 
            "# First line.\n" +
            "# Second line that is quite long and needs to be wrapped.";
        expect(formatComment(inputString, 60)).toBe(expectedOutput);
    });

    it('test with a line that is exactly max_length characters long', () => {
        const inputString = "A".repeat(60); // 60 characters long
        const expectedOutput = "# " + "A".repeat(60);
        expect(formatComment(inputString, 60)).toBe(expectedOutput);
    });

    it('test with an empty string', () => {
        const inputString = "";
        const expectedOutput = "# ";
        expect(formatComment(inputString)).toBe(expectedOutput);
    });
});
