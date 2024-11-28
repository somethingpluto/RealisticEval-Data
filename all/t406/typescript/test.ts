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

  describe('Combined Colors', () => {
    it('test_combined_colors', () => {
      const inputTextRed = Colors.red('Red');
      const inputTextBlue = Colors.blue('Blue');
      const inputTextCombined = `${inputTextRed} and ${inputTextBlue}`;
      const expectedOutput = '\x1b[91mRed\x1b[0m and \x1b[94mBlue\x1b[0m';
      expect(inputTextCombined).toEqual(expectedOutput);
    });
  });
});