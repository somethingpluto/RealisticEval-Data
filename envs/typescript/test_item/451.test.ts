// ... (previous code for context)
import { Jimp } from 'jimp';
import { promisify } from 'util';
import { readFile } from 'fs/promises';

const readFileAsync = promisify(readFile);

async function convertImageToBits(imagePath: string): Promise<number[]> {
  try {
    const imageBuffer = await readFileAsync(imagePath);
    const image = await Jimp.read(imageBuffer);
    // ... (rest of the function)
  } catch (error) {
    throw new Error(`Failed to read image: ${error.message}`);
  }
}
// ... (rest of the code)
import Jimp from 'jimp';

describe('TestConvertImageToBits', () => {
    let whiteImagePath: string;
    let blackImagePath: string;
    let mixedImagePath: string;
    let largeImagePath: string;

    beforeEach(() => {
        // Create test images before each test
        whiteImagePath = 'white_image.bmp';
        blackImagePath = 'black_image.bmp';
        mixedImagePath = 'mixed_image.bmp';
        largeImagePath = 'large_image.bmp';

        // Create a white image (all pixels white)
        const whiteImage = new Jimp(2, 2, 0xffffffff); // 0xffffffff is white
        whiteImage.write(whiteImagePath);

        // Create a black image (all pixels black)
        const blackImage = new Jimp(2, 2, 0x00000000); // 0x00000000 is black
        blackImage.write(blackImagePath);

        // Create a mixed image (half white, half black)
        const mixedImage = new Jimp(2, 2);
        mixedImage.setPixelColor(0xffffffff, 0, 0); // White
        mixedImage.setPixelColor(0x00000000, 0, 1); // Black
        mixedImage.setPixelColor(0x00000000, 1, 0); // Black
        mixedImage.setPixelColor(0xffffffff, 1, 1); // White
        mixedImage.write(mixedImagePath);

        // Create a larger image (3x3)
        const largeImage = new Jimp(3, 3);
        largeImage.setPixelColor(0xffffffff, 0, 0); // White
        largeImage.setPixelColor(0xffffffff, 1, 1); // White
        largeImage.setPixelColor(0xffffffff, 2, 2); // White
        largeImage.write(largeImagePath);
    });

    afterEach(() => {
        // Remove the test images after each test
        require('fs').unlinkSync(whiteImagePath);
        require('fs').unlinkSync(blackImagePath);
        require('fs').unlinkSync(mixedImagePath);
        require('fs').unlinkSync(largeImagePath);
    });

    it('test converting a white image', async () => {
        const expectedOutput = [1, 1, 1, 1]; // All pixels should be 1 (white)
        const result = await convertImageToBits(whiteImagePath);
        expect(result).toEqual(expectedOutput);
    });

    it('test converting a black image', async () => {
        const expectedOutput = [0, 0, 0, 0]; // All pixels should be 0 (black)
        const result = await convertImageToBits(blackImagePath);
        expect(result).toEqual(expectedOutput);
    });

    it('test converting a mixed image', async () => {
        const expectedOutput = [1, 0, 0, 1]; // 1 white, 3 black
        const result = await convertImageToBits(mixedImagePath);
        expect(result).toEqual(expectedOutput);
    });

    it('test converting an invalid image path', async () => {
        await expect(convertImageToBits('invalid_image_path.bmp')).rejects.toThrow(/ENOENT/);
    });

    it('test converting a larger image', async () => {
        const expectedOutput = [
            1, 0, 0,
            0, 1, 0,
            0, 0, 1
        ];
        const result = await convertImageToBits(largeImagePath);
        expect(result).toEqual(expectedOutput);
    });
});
