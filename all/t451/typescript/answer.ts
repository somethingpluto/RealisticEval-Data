import * as fs from 'fs';
import { createReadStream } from 'stream';
import * as sharp from 'sharp';

async function convertImageToBits(imagePath: string): Promise<number[]> {
    /*
    Converts an image to a binary representation. Convert the image to black and white mode,
    that is, each pixel is represented by only 1 bit, with a white pixel value of 255 and a black pixel value of 0

    Args:
        imagePath (string): The file path of the image to convert.

    Returns:
        number[]: A list of bits representing the image, where 1 is for white pixels
              and 0 is for black pixels.
    */

    const stream = createReadStream(imagePath);
    const buffer: Buffer[] = [];

    return new Promise((resolve, reject) => {
        stream.on('data', chunk => buffer.push(chunk));
        stream.on('end', async () => {
            try {
                const imgData = await sharp(buffer[0]).greyscale().raw().toBuffer();
                const width = Math.sqrt(imgData.length / 3); // Assuming RGB format
                const bits: number[] = [];

                for (let i = 0; i < imgData.length; i += 3) {
                    const r = imgData[i];
                    const g = imgData[i + 1];
                    const b = imgData[i + 2];

                    // Calculate average brightness
                    const avgBrightness = (r + g + b) / 3;

                    if (avgBrightness > 127) {
                        bits.push(1);
                    } else {
                        bits.push(0);
                    }
                }

                resolve(bits);
            } catch (error) {
                reject(error);
            }
        });
        stream.on('error', error => reject(error));
    });
}