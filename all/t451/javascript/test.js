const { convertImageToBits } = require('./path-to-your-function'); // Adjust the import accordingly

describe('convertImageToBits', () => {
  it('should convert an image to a binary representation', async () => {
    const imagePath = 'path/to/your/image.jpg'; // Replace with actual image path
    const expectedResult = [0, 1, 0, 1]; // Replace with expected result based on your image

    const result = await convertImageToBits(imagePath);

    expect(result).toEqual(expectedResult);
  });
});
