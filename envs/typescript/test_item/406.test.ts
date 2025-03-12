// ... (previous code for context)
    static red(text: string): string {
        return `\x1b[31m${text}\x1b[0m`;
    }

    static green(text: string): string {
        return `\x1b[32m${text}\x1b[0m`;
    }

    static blue(text: string): string {
        return `\x1b[34m${text}\x1b[0m`;
    }

    static yellow(text: string): string {
        return `\x1b[33m${text}\x1b[0m`;
    }

    static magenta(text: string): string {
        return `\x1b[35m${text}\x1b[0m`;
    }

    static cyan(text: string): string {
        return `\x1b[36m${text}\x1b[0m`;
    }

    static rainbow(text: string): string {
        const colors = ['\x1b[31m', '\x1b[33m', '\x1b[32m', '\x1b[36m', '\x1b[35m'];
        let rainbowText = '';
        for (let i = 0; i < text.length; i++) {
            rainbowText += colors[i % colors.length] + text[i];
        }
        return rainbowText + '\x1b[0m';
    }
}
// ... (rest of the class)
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
