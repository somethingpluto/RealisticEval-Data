const Jimp = require('jimp');

/**
 * Converts an image to a binary representation.
 * Convert the image to black and white mode, that is, each pixel is represented by only 1 bit,
 * with a white pixel value of 255 and a black pixel value of 0.
 *
 * @param {string} imagePath - The file path of the image to convert.
 * @returns {Promise<Array<number>>} A promise that resolves to an array of bits representing the image,
 *                                   where 1 is for white pixels and 0 is for black pixels.
 */
async function convertImageToBits(imagePath) {
  try {
    const image = await Jimp.read(imagePath);
    image.grayscale(); // Convert image to grayscale
    const binaryData = [];

    // Iterate over each pixel in the image
    for (let y = 0; y < image.bitmap.height; y++) {
      for (let x = 0; x < image.bitmap.width; x++) {
        const pixel = image.getPixelColor(x, y);
        const { r, g, b } = Jimp.intToRGBA(pixel);
        // Check if the pixel is white
        if (r === 255 && g === 255 && b === 255) {
          binaryData.push(1);
        } else {
          binaryData.push(0);
        }
      }
    }

    return binaryData;
  } catch (error) {
    console.error('Error converting image to bits:', error);
    throw error;
  }
}
const fs = require('fs');
const Jimp = require('jimp');

describe('TestConvertImageToBits', () => {
    let white_image_path = 'white_image.bmp';
    let black_image_path = 'black_image.bmp';
    let mixed_image_path = 'mixed_image.bmp';

    beforeEach(() => {
        // Create a white image (all pixels white)
        Jimp.create(2, 2, 0xffffff).write(white_image_path);

        // Create a black image (all pixels black)
        Jimp.create(2, 2, 0x000000).write(black_image_path);

        // Create a mixed image (half white, half black)
        const mixedImage = new Jimp(2, 2);
        mixedImage.setPixelColor(0xffffff, 0, 0); // White
        mixedImage.setPixelColor(0x000000, 0, 1); // Black
        mixedImage.setPixelColor(0x000000, 1, 0); // Black
        mixedImage.setPixelColor(0xffffff, 1, 1); // White
        mixedImage.write(mixed_image_path);
    });

    afterEach(() => {
        fs.unlinkSync(white_image_path);
        fs.unlinkSync(black_image_path);
        fs.unlinkSync(mixed_image_path);
    });

    it('test_white_image', async () => {
        const expected_output = [1, 1, 1, 1];  // All pixels should be 1 (white)
        const result = await convertImageToBits(white_image_path);
        expect(result).toEqual(expected_output);
    });

    it('test_black_image', async () => {
        const expected_output = [0, 0, 0, 0];  // All pixels should be 0 (black)
        const result = await convertImageToBits(black_image_path);
        expect(result).toEqual(expected_output);
    });

    it('test_mixed_image', async () => {
        const expected_output = [1, 0, 0, 1];  // 1 white, 3 black
        const result = await convertImageToBits(mixed_image_path);
        expect(result).toEqual(expected_output);
    });

    it('test_invalid_image_path', async () => {
        try {
            await convertImageToBits('invalid_image_path.bmp');
        } catch (error) {
            expect(error.code).toBe('ENOENT');
        }
    });

    it('test_large_image', async () => {
        const large_image_path = 'large_image.bmp';
        const largeImage = new Jimp(3, 3);
        largeImage.setPixelColor(0xffffff, 0, 0); // White
        largeImage.setPixelColor(0xffffff, 1, 1); // White
        largeImage.setPixelColor(0xffffff, 2, 2); // White
        largeImage.write(large_image_path);

        const expected_output = [
            1, 0, 0,
            0, 1, 0,
            0, 0, 1
        ];
        const result = await convertImageToBits(large_image_path);
        expect(result).toEqual(expected_output);

        // Clean up
        fs.unlinkSync(large_image_path);
    });
});
