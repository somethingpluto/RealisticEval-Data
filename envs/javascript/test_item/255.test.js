const Jimp = require('jimp');

/**
 * Converts an image to an array of binary bits. The image is converted to black and white mode,
 * where white pixels (value 255) are represented by 1 and black pixels by 0. These bits are then
 * stored in an array and returned.
 *
 * @param {string} imagePath - The path to the image file.
 * @returns {Promise<Array<number>>} A promise that resolves to an array of bits (0 or 1) representing the image.
 */
async function convertImageToBits(imagePath) {
    try {
        // Load the image
        const image = await Jimp.read(imagePath);

        // Convert the image to black and white mode
        image.greyscale();

        // Get the width and height of the image
        const width = image.getWidth();
        const height = image.getHeight();

        // Initialize an array to store the bits
        const bits = [];

        // Iterate over each pixel in the image
        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                // Get the color of the pixel
                const pixelColor = Jimp.intToRGBA(image.getPixelColor(x, y));

                // Determine the bit value based on the pixel color
                const bit = pixelColor.r === 255 ? 1 : 0;

                // Add the bit to the array
                bits.push(bit);
            }
        }

        // Return the array of bits
        return bits;
    } catch (error) {
        throw new Error(`Failed to convert image to bits: ${error.message}`);
    }
}
const Jimp = require('jimp');
const fs = require('fs');
const { Readable } = require('stream');

jest.mock('./convertImageToBits', () => ({
  convertImageToBits: jest.fn(),
}));


describe('TestConvertImageToBits', () => {
  function createImage(mode, size, color) {
    /**
     * Helper method to create an in-memory image.
     *
     * @param {string} mode - The color mode of the image (e.g., '1' for binary, 'L' for grayscale).
     * @param {Array<number>} size - An array of the image size [width, height].
     * @param {number} color - The color to fill the image. 255 for white, 0 for black in '1' mode.
     *
     * @returns {Promise<Jimp>} A Promise that resolves to a Jimp Image object.
     */
    return Jimp.create(size[0], size[1], color).then((image) => {
      if (mode === '1') {
        image.grayscale();
        image.threshold(127);
      }
      return image;
    });
  }

  async function getImageBytes(image) {
    const buffer = await image.getBufferAsync(Jimp.MIME_PNG);
    return new Readable().wrap(buffer);
  }

  describe('test_all_white_image', () => {
    it('should convert an all-white image correctly', async () => {
      const image = await createImage('1', [4, 4], 0xffffff); // White color in RGB
      const imgBytes = await getImageBytes(image);
      const expectedBits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
      const result = await convertImageToBits(imgBytes);
      expect(result).toEqual(expectedBits);
    });
  });

  describe('test_all_black_image', () => {
    it('should convert an all-black image correctly', async () => {
      const image = await createImage('1', [4, 4], 0x000000); // Black color in RGB
      const imgBytes = await getImageBytes(image);
      const expectedBits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
      const result = await convertImageToBits(imgBytes);
      expect(result).toEqual(expectedBits);
    });
  });

  describe('test_checkerboard_image', () => {
    it('should convert a checkerboard image correctly', async () => {
      const image = await createImage('1', [4, 4], 0x000000); // Black color in RGB
      const pixels = image.bitmap.data;
      for (let y = 0; y < 4; y++) {
        for (let x = 0; x < 4; x++) {
          if ((x + y) % 2 === 0) {
            const index = (y * 4 + x) * 4;
            pixels[index] = 255; // Red channel
            pixels[index + 1] = 255; // Green channel
            pixels[index + 2] = 255; // Blue channel
            pixels[index + 3] = 255; // Alpha channel
          }
        }
      }
      const imgBytes = await getImageBytes(image);
      const expectedBits = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1];
      const result = await convertImageToBits(imgBytes);
      expect(result).toEqual(expectedBits);
    });
  });

  describe('test_horizontal_stripes_image', () => {
    it('should convert a horizontal stripes image correctly', async () => {
      const image = await createImage('1', [4, 4], 0x000000); // Black color in RGB
      const pixels = image.bitmap.data;
      for (let y = 0; y < 4; y++) {
        for (let x = 0; x < 4; x++) {
          if (y % 2 === 0) {
            const index = (y * 4 + x) * 4;
            pixels[index] = 255; // Red channel
            pixels[index + 1] = 255; // Green channel
            pixels[index + 2] = 255; // Blue channel
            pixels[index + 3] = 255; // Alpha channel
          }
        }
      }
      const imgBytes = await getImageBytes(image);
      const expectedBits = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0];
      const result = await convertImageToBits(imgBytes);
      expect(result).toEqual(expectedBits);
    });
  });

  describe('test_vertical_stripes_image', () => {
    it('should convert a vertical stripes image correctly', async () => {
      const image = await createImage('1', [4, 4], 0x000000); // Black color in RGB
      const pixels = image.bitmap.data;
      for (let y = 0; y < 4; y++) {
        for (let x = 0; x < 4; x++) {
          if (x % 2 === 0) {
            const index = (y * 4 + x) * 4;
            pixels[index] = 255; // Red channel
            pixels[index + 1] = 255; // Green channel
            pixels[index + 2] = 255; // Blue channel
            pixels[index + 3] = 255; // Alpha channel
          }
        }
      }
      const imgBytes = await getImageBytes(image);
      const expectedBits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0];
      const result = await convertImageToBits(imgBytes);
      expect(result).toEqual(expectedBits);
    });
  });
});
