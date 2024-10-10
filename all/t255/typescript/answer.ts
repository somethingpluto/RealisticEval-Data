import { createCanvas, loadImage } from 'canvas';

interface BitArray {
  [index: number]: number;
}

async function convertImageToBits(imagePath: string): Promise<BitArray> {
  /**
   * Convert a picture to an array of binary bits. Convert it to black and white mode (only 0s and 1s, corresponding to black and white),
   * convert the white pixel (value 255) to 1, convert the black pixel to 0, and finally store these bits in an array and return.
   *
   * @param imagePath - The path to the image file.
   * @returns A promise that resolves with a list of bits (0 or 1) representing the image.
   */

  const canvas = createCanvas(1, 1);
  const ctx = canvas.getContext('2d');

  try {
    const img = await loadImage(imagePath);
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img, 0, 0);

    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;

    const bitArray: BitArray = [];

    for (let i = 0; i < data.length; i += 4) {
      // Each pixel has 4 values (RGBA)
      const r = data[i];
      const g = data[i + 1];
      const b = data[i + 2];

      // Convert to grayscale by averaging RGB values
      const gray = Math.round((r + g + b) / 3);

      // Convert to binary bit
      const bit = gray > 127 ? 1 : 0;

      bitArray.push(bit);
    }

    return bitArray;
  } catch (error) {
    throw new Error(`Error converting image to bits: ${error}`);
  }
}