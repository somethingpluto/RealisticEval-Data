describe('convertImageToBits', () => {
  it('should convert a simple black and white image to binary bits', async () => {
    // Mocking the image data (this should be replaced with actual image data loading logic)
    const mockImageData = [
      [0, 0, 0], // Black
      [255, 255, 255] // White
    ];

    // Mock the image processing logic (this should be replaced with actual image processing logic)
    const mockConvertImageDataToBits = jest.fn(() => [0, 1]);

    // Replace the real implementation with the mock
    const realConvertImageToBits = convertImageToBits;
    convertImageToBits = mockConvertImageDataToBits;

    try {
      const result = await convertImageToBits(mockImageData);
      expect(result).toEqual([0, 1]);
    } finally {
      // Restore the real implementation after the test
      convertImageToBits = realConvertImageToBits;
    }
  });

  it('should handle edge cases', async () => {
    // Test with empty image data
    const emptyImageData = [];
    expect(await convertImageToBits(emptyImageData)).toEqual([]);

    // Test with non-binary values
    const invalidImageData = [[256, 0, 0]];
    expect(() => convertImageToBits(invalidImageData)).toThrowError('Invalid image data');
  });
});