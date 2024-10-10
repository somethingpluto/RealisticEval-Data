describe('moveEmojisToEnd', () => {
    it('should move emojis to the end of the string', () => {
        expect(moveEmojisToEnd('Hello, World! 😊')).toBe('Hello, World! 😊');
        expect(moveEmojisToEnd('Hello, 🌍! 😊')).toBe('Hello, ! 🌍😊');
        expect(moveEmojisToEnd('Hello, 🌍! 🌐')).toBe('Hello, ! 🌍🌐');
        expect(moveEmojisToEnd('Hello, 🌍! 😀')).toBe('Hello, ! 😀🌍');
        expect(moveEmojisToEnd('Hello, 🌍! 😊😀')).toBe('Hello, ! 😊😀🌍');
        expect(moveEmojisToEnd('Hello, 🌍! 😊😀🙂')).toBe('Hello, ! 😊😀🙂🌍');
    });

    it('should handle strings without emojis', () => {
        expect(moveEmojisToEnd('Hello, World! ')).toBe('Hello, World! ');
        expect(moveEmojisToEnd('Hello, World!')).toBe('Hello, World!');
        expect(moveEmojisToEnd('Hello, World! ')).toBe('Hello, World! ');
        expect(moveEmojisToEnd('Hello, World!')).toBe('Hello, World!');
    });
});