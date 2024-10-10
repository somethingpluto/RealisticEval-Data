describe('moveEmojisToEnd', () => {
    test('moves emojis to the end of the text', () => {
      expect(moveEmojisToEnd("Hello, World! 😊")).toBe("Hello, World!😊");
      expect(moveEmojisToEnd("Python 🐍 is fun!")).toBe("Python is fun!PYTHON");
      expect(moveEmojisToEnd("No emojis here.")).toBe("No emojis here.");
      expect(moveEmojisToEnd("")).toBe("");
    });
  });