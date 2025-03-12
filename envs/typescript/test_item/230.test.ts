import { isEmoji } from 'emoji-regex';

function moveEmojisToEnd(text: string): string {
  const emojiRegex = /[\uD800-\uDBFF][\uDC00-\uDFFF]|[\u2600-\u26FF\u2700-\u27BF]/gu;
  const emojis = text.match(emojiRegex) || [];
  const textWithoutEmojis = text.replace(emojiRegex, '');
  return textWithoutEmojis + emojis.join('');
}
describe('TestMoveEmojisToEnd', () => {
    it('should handle strings with no emojis', () => {
        const inputText = "This is a test.";
        const expectedOutput = "This is a test.";
        expect(moveEmojisToEnd(inputText)).toEqual(expectedOutput);
    });

    it('should handle strings with only emojis', () => {
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
