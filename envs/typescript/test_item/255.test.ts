// ... (previous code for context)
import { Jimp } from 'jimp';
import { promisify } from 'util';
import { readFile } from 'fs/promises';

const readFileAsync = promisify(readFile);

async function convertImageToBits(imagePath: string): Promise<number[]> {
  try {
    const imageBuffer = await readFileAsync(imagePath);
    const image = await Jimp.read(imageBuffer);
    // ... (rest of the function remains the same)
  } catch (error) {
    console.error('Error reading the image:', error);
    throw error;
  }
}
// ... (rest of the code for context)
import Jimp from 'jimp';
describe('TestConvertImageToBits', () => {
    /**
     * Helper method to create an in-memory image.
     *
     * @param {string} mode - The color mode of the image (e.g., '1' for binary, 'L' for grayscale).
     * @param {number[]} size - A tuple of the image size (width, height).
     * @param {number | number[]} color - The color to fill the image. 255 for white, 0 for black in '1' mode.
     * @returns {Promise<Jimp>} A Jimp Image object.
     */
    async function createImage(mode: string, size: [number, number], color: number | number[]): Promise<Jimp> {
        const image = new Jimp(size[0], size[1], color);
        if (mode === '1') {
            image.color([{ apply: 'greyscale', params: [] }]);
        }
        return image;
    }

    describe('test_all_white_image', () => {
        it('should convert an all-white image to bits', async () => {
            const image = await createImage('1', [4, 4], 0xffffff); // White color in RGB
            const imgBuffer = await image.getBufferAsync(Jimp.MIME_PNG);
            const result = await convertImageToBits(imgBuffer);
            const expectedBits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
            expect(result).toEqual(expectedBits);
        });
    });

    describe('test_all_black_image', () => {
        it('should convert an all-black image to bits', async () => {
            const image = await createImage('1', [4, 4], 0x000000); // Black color in RGB
            const imgBuffer = await image.getBufferAsync(Jimp.MIME_PNG);
            const result = await convertImageToBits(imgBuffer);
            const expectedBits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
            expect(result).toEqual(expectedBits);
        });
    });

    describe('test_checkerboard_image', () => {
        it('should convert a checkerboard image to bits', async () => {
            const image = await createImage('1', [4, 4], 0x000000); // Black color in RGB
            for (let y = 0; y < 4; y++) {
                for (let x = 0; x < 4; x++) {
                    if ((x + y) % 2 === 0) {
                        image.setPixelColor(0xffffff, x, y); // Set white pixel
                    }
                }
            }
            const imgBuffer = await image.getBufferAsync(Jimp.MIME_PNG);
            const result = await convertImageToBits(imgBuffer);
            const expectedBits = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1];
            expect(result).toEqual(expectedBits);
        });
    });

    describe('test_horizontal_stripes_image', () => {
        it('should convert a horizontal stripes image to bits', async () => {
            const image = await createImage('1', [4, 4], 0x000000); // Black color in RGB
            for (let y = 0; y < 4; y++) {
                for (let x = 0; x < 4; x++) {
                    if (y % 2 === 0) {
                        image.setPixelColor(0xffffff, x, y); // Set white pixel
                    }
                }
            }
            const imgBuffer = await image.getBufferAsync(Jimp.MIME_PNG);
            const result = await convertImageToBits(imgBuffer);
            const expectedBits = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0];
            expect(result).toEqual(expectedBits);
        });
    });

    describe('test_vertical_stripes_image', () => {
        it('should convert a vertical stripes image to bits', async () => {
            const image = await createImage('1', [4, 4], 0x000000); // Black color in RGB
            for (let y = 0; y < 4; y++) {
                for (let x = 0; x < 4; x++) {
                    if (x % 2 === 0) {
                        image.setPixelColor(0xffffff, x, y); // Set white pixel
                    }
                }
            }
            const imgBuffer = await image.getBufferAsync(Jimp.MIME_PNG);
            const result = await convertImageToBits(imgBuffer);
            const expectedBits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0];
            expect(result).toEqual(expectedBits);
        });
    });
});
