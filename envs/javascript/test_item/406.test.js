class Colors {
    // text in red color
    static red(text) {
        return `<span style="color:red;">${text}</span>`;
    }

    // text in green color
    static green(text) {
        return `<span style="color:green;">${text}</span>`;
    }

    // text in blue color
    static blue(text) {
        return `<span style="color:blue;">${text}</span>`;
    }

    // text in yellow color
    static yellow(text) {
        return `<span style="color:yellow;">${text}</span>`;
    }

    // text in magenta color
    static magenta(text) {
        return `<span style="color:magenta;">${text}</span>`;
    }

    // text in cyan color
    static cyan(text) {
        return `<span style="color:cyan;">${text}</span>`;
    }
}
describe('Colors', () => {
  describe('Color Methods', () => {
    it('test_red', () => {
      const inputText = 'Hello';
      const expectedOutput = '\x1b[91mHello\x1b[0m';
      expect(Colors.red(inputText)).toEqual(expectedOutput);
    });

    it('test_green', () => {
      const inputText = 'Hello';
      const expectedOutput = '\x1b[92mHello\x1b[0m';
      expect(Colors.green(inputText)).toEqual(expectedOutput);
    });

    it('test_blue', () => {
      const inputText = 'Hello';
      const expectedOutput = '\x1b[94mHello\x1b[0m';
      expect(Colors.blue(inputText)).toEqual(expectedOutput);
    });

    it('test_yellow', () => {
      const inputText = 'Hello';
      const expectedOutput = '\x1b[93mHello\x1b[0m';
      expect(Colors.yellow(inputText)).toEqual(expectedOutput);
    });

    it('test_magenta', () => {
      const inputText = 'Hello';
      const expectedOutput = '\x1b[95mHello\x1b[0m';
      expect(Colors.magenta(inputText)).toEqual(expectedOutput);
    });

    it('test_cyan', () => {
      const inputText = 'Hello';
      const expectedOutput = '\x1b[96mHello\x1b[0m';
      expect(Colors.cyan(inputText)).toEqual(expectedOutput);
    });
  });
});
