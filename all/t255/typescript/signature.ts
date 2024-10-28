import Jimp from 'jimp';

/**
 * Converts an image to an array of binary bits.
 * Converts the image to black and white mode (only 0s and 1s, corresponding to black and white),
 * converts the white pixel (value 255) to 1, converts the black pixel to 0,
 * and finally stores these bits in an array and returns it.
 *
 * @param {string} imagePath - The path to the image file.
 * @returns {Promise<number[]>} A promise that resolves to a list of bits (0 or 1) representing the image.
 */
async function convertImageToBits(imagePath: string): Promise<number[]> {}