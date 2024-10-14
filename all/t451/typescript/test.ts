import { describe, expect, it } from '@jest/globals';
import { convertImageToBits } from './path-to-your-module'; // Adjust the import according to your module structure

describe('convertImageToBits', () => {
  it('should convert a simple 2x2 black and white image to bits', () => {
    const imagePath = 'path/to/test/black-and-white-image.png'; // Replace with a valid path to a black and white image
    const expectedBits = [0, 0, 0, 0]; // Expected bits for a 2x2 black image

    const result = convertImageToBits(imagePath);

    expect(result).toEqual(expectedBits);
  });

  it('should convert a simple 2x2 image with one white and three black pixels to bits', () => {
    const imagePath = 'path/to/test/one-white-three-black-image.png'; // Replace with a valid path to such an image
    const expectedBits = [1, 0, 0, 0]; // Expected bits for a 2x2 image with one white pixel

    const result = convertImageToBits(imagePath);

    expect(result).toEqual(expectedBits);
  });
});