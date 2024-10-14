const fs = require('fs');
const sharp = require('sharp');

function convertImageToBits(imagePath) {
    return new Promise((resolve, reject) => {
        sharp(imagePath)
            .greyscale()
            .raw()
            .toBuffer((err, data, info) => {
                if (err) {
                    return reject(err);
                }

                const bits = [];
                for (let i = 0; i < data.length; i += 3) {
                    // Convert RGB to grayscale
                    const gray = Math.round(0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2]);

                    // Convert grayscale to binary
                    const binary = gray > 127 ? '1' : '0';
                    bits.push(parseInt(binary));
                }

                resolve(bits);
            });
    });
}

// Usage example:
convertImageToBits('path/to/your/image.jpg')
    .then(bits => console.log(bits))
    .catch(err => console.error(err));