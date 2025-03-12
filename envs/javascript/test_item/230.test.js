/**
 * Move the emoji expressions in the string to the end of the text.
 *
 * @param {string} text - The input string containing text and possibly emojis.
 * @returns {string} - The modified string with all emojis moved to the end.
 */
function moveEmojisToEnd(text) {
    // Regular expression to match emojis
    const emojiRegex = /[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{1F900}-\u{1F9FF}\u{1F1E0}-\u{1F1FF}]/gu;

    // Extract all emojis from the text
    const emojis = text.match(emojiRegex) || [];

    // Remove all emojis from the text
    const textWithoutEmojis = text.replace(emojiRegex, '');

    // Concatenate the text without emojis with the extracted emojis
    return textWithoutEmojis + emojis.join('');
}
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
