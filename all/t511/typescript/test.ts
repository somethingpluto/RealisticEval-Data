describe('TestHexToAnsi', () => {
    describe('testValidColors', () => {
        it('should correctly convert valid hex color inputs', () => {
            expect(hexToAnsi('#FF5733')).toBe('\x1b[38;2;255;87;51m');
            expect(hexToAnsi('#00FF00')).toBe('\x1b[38;2;0;255;0m');
            expect(hexToAnsi('#0000FF')).toBe('\x1b[38;2;0;0;255m');
        });
    });

    describe('testBlackAndWhite', () => {
        it('should correctly handle black and white colors', () => {
            expect(hexToAnsi('#000000')).toBe('\x1b[38;2;0;0;0m'); // Black
            expect(hexToAnsi('#FFFFFF')).toBe('\x1b[38;2;255;255;255m'); // White
        });
    });
});