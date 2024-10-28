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