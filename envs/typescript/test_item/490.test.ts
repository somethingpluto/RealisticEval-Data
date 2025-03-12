// ... (previous code for context)

function formatStr(x: any): string {
  if (typeof x === 'string') {
    return x.replace(/
describe('TestFormatStr', () => {
  it('test simple string', () => {
    /** Test a simple string input. */
    const inputStr = "Hello, World!";
    const expectedOutput = "> Hello, World!";
    expect(formatStr(inputStr)).toEqual(expectedOutput);
  });

  it('test multiline string', () => {
    /** Test a multiline string input. */
    const inputStr = "Line 1\nLine 2\nLine 3";
    const expectedOutput = "> Line 1\n> Line 2\n> Line 3";
    expect(formatStr(inputStr)).toEqual(expectedOutput);
  });

  it('test code block delimiters even', () => {
    /** Test a string with an even number of code block delimiters. */
    const inputStr = "Some code:\n```\nprint('Hello')\n```";
    const expectedOutput = "> Some code:\n> ```\n> print('Hello')\n> ```";
    expect(formatStr(inputStr)).toEqual(expectedOutput);
  });

  it('test code block delimiters odd', () => {
    /** Test a string with an odd number of code block delimiters. */
    const inputStr = "Some code:\n```\nprint('Hello')";
    const expectedOutput = "> Some code:\n> ```\n> print('Hello')\n> ```";
    expect(formatStr(inputStr)).toEqual(expectedOutput);
  });

  it('test non-string input', () => {
    /** Test non-string input (e.g., integer) to ensure it's converted. */
    const inputValue = 123;
    const expectedOutput = "> 123";
    expect(formatStr(inputValue)).toEqual(expectedOutput);
  });
});
