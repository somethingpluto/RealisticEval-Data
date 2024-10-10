describe('convertImageToBits', () => {
    test('should convert a black pixel to 0', async () => {
        const result = await convertImageToBits('./path/to/black-pixel-image.png');
        expect(result).toContain(0);
    });

    test('should convert a white pixel to 1', async () => {
        const result = await convertImageToBits('./path/to/white-pixel-image.png');
        expect(result).toContain(1);
    });
});