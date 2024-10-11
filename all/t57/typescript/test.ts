describe('convert_png_to_ico', () => {
  it('should convert a PNG file to an ICO file with specified sizes', async () => {
    const pngFilePath = 'path/to/source.png';
    const icoFilePath = 'path/to/output.ico';
    const iconSizes = [(32, 32)];

    await convert_png_to_ico(pngFilePath, icoFilePath, iconSizes);

    // Assuming there is some way to verify if the ICO file was created successfully
    // For example, checking if the file exists at the specified path
    expect(icoFilePath).toBeExist(); // This is a hypothetical method to check file existence
  });

  it('should handle different icon sizes', async () => {
    const pngFilePath = 'path/to/source.png';
    const icoFilePath = 'path/to/output.ico';
    const iconSizes = [(32, 32), (64, 64), (128, 128)];

    await convert_png_to_ico(pngFilePath, icoFilePath, iconSizes);

    // Similarly, verify if the ICO file contains all the specified sizes
    // For example, checking if the file size matches the expected size
    expect(icoFilePath).toBeSizeOf(3 * /* expected size */); // Hypothetical method to check file size
  });
});