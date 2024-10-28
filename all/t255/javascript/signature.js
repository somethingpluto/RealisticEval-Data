const Jimp = require('jimp');

/**
 * Converts an image to an array of binary bits. The image is converted to black and white mode,
 * where white pixels (value 255) are represented by 1 and black pixels by 0. These bits are then
 * stored in an array and returned.
 *
 * @param {string} imagePath - The path to the image file.
 * @returns {Promise<Array<number>>} A promise that resolves to an array of bits (0 or 1) representing the image.
 */
async function convertImageToBits(imagePath) {}