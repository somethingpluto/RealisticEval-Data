const fs = require('fs');
const path = require('path');

function countUniqueColors(imagePath) {
    /**
     * Count the number of unique colors in an image.
     *
     * @param {string} imagePath - Path to the image file.
     * @returns {Promise<number>} - The number of unique colors in the image.
     */
    
    return new Promise((resolve, reject) => {
        const imageBuffer = fs.readFileSync(imagePath);
        
        // Using sharp library to handle image processing
        const sharp = require('sharp');
        sharp(imageBuffer)
            .raw()
            .toBuffer()
            .then(data => {
                const width = 100; // Assuming a fixed width for simplicity
                const height = data.length / (width * 3); // Assuming RGB format
                const colorSet = new Set();
                
                for (let i = 0; i < data.length; i += 3) {
                    const r = data[i];
                    const g = data[i + 1];
                    const b = data[i + 2];
                    const colorKey = `${r},${g},${b}`;
                    colorSet.add(colorKey);
                }
                
                resolve(colorSet.size);
            })
            .catch(err => {
                reject(err);
            });
    });
}