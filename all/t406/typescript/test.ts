describe('Colors', () => {
  it('test_red', () => {
    const inputText = 'Hello';
    const expectedOutput = '\033[91mHello\033[0m';
    expect(Colors.red(inputText)).toBe(expectedOutput);
  });

  it('test_green', () => {
    const inputText = 'Hello';
    const expectedOutput = '\033[92mHello\033[0m';
    expect(Colors.green(inputText)).toBe(expectedOutput);
  });

  it('test_blue', () => {
    const inputText = 'Hello';
    const expectedOutput = '\033[94mHello\033[0m';
    expect(Colors.blue(inputText)).toBe(expectedOutput);
  });

  it('test_yellow', () => {
    const inputText = 'Hello';
    const expectedOutput = '\033[93mHello\033[0m';
    expect(Colors.yellow(inputText)).toBe(expectedOutput);
  });

  it('test_magenta', () => {
    const inputText = 'Hello';
    const expectedOutput = '\033[95mHello\033[0m';
    expect(Colors.magenta(inputText)).toBe(expectedOutput);
  });

  it('test_cyan', () => {
    const inputText = 'Hello';
    const expectedOutput = '\033[96mHello\033[0m';
    expect(Colors.cyan(inputText)).toBe(expectedOutput);
  });
});