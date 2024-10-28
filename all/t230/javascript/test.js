describe('TestMoveEmojisToEnd', () => {
  it('should handle a string with no emojis', () => {
      const inputText = "This is a test.";
      const expectedOutput = "This is a test.";
      expect(moveEmojisToEnd(inputText)).toEqual(expectedOutput);
  });

  it('should handle a string with only emojis', () => {
      const inputText = "😀😃😄😁";
      const expectedOutput = "😀😃😄😁";
      expect(moveEmojisToEnd(inputText)).toEqual(expectedOutput);
  });

  it('should handle emojis at the start of the text', () => {
      const inputText = "😀😃Hello world!";
      const expectedOutput = "Hello world!😀😃";
      expect(moveEmojisToEnd(inputText)).toEqual(expectedOutput);
  });

  it('should handle emojis already at the end of the text', () => {
      const inputText = "Hello world!😀😃";
      const expectedOutput = "Hello world!😀😃";
      expect(moveEmojisToEnd(inputText)).toEqual(expectedOutput);
  });

  it('should handle emojis in the middle of the text', () => {
      const inputText = "Hello 😀world😃!";
      const expectedOutput = "Hello world!😀😃";
      expect(moveEmojisToEnd(inputText)).toEqual(expectedOutput);
  });

  it('should handle text with mixed characters and emojis', () => {
      const inputText = "Hi! 😀 How are you? 😃";
      const expectedOutput = "Hi!  How are you? 😀😃";
      expect(moveEmojisToEnd(inputText)).toEqual(expectedOutput);
  });
});