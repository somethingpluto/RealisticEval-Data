const fs = require('fs');
const Jimp = require('jimp');

async function convertImageToBits(imagePath) {
    let image;

    try {
        image = await Jimp.read(imagePath);
    } catch (error) {
        console.error("Error reading the image:", error);
        return [];
    }

    const width = image.bitmap.width;
    const height = image.bitmap.height;
    const bits = [];

    for(let y=0; y<height; y++) {
        for(let x=0; x<width; x++) {
            const rgba = image.getPixelColor(x, y);
            const red = (rgba >> 24) & 0xff;

            // Assuming white pixels have a value of 255, we'll convert them to 1
            // and black pixels with a value of 0 to 0
            bits.push(red === 255 ? 1 : 0);
        }
    }

    return bits;
}