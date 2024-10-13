const sharp = require('sharp');
const iconv = require('iconv');

/**
 * Convert a PNG image file to an ICO format file.
 *
 * @param {string} pngFilePath - Path to the source PNG image file.
 * @param {string} icoFilePath - Path to save the ICO file.
 * @param {Array} iconSizes - Array of tuples specifying the sizes to include in the ICO file.
 */
async function convertPngToIco(pngFilePath, icoFilePath, iconSizes = [[32, 32]]) {
    try {
        // Load the PNG image using sharp
        const img = await sharp(pngFilePath);

        // Resize the image to the specified sizes
        const resizedImages = iconSizes.map(size => img.resize(size[0], size[1]));

        // Convert the resized images to ICO format
        const icoBuffer = await Promise.all(resizedImages).then(images => {
            return iconv.toIco(images);
        });

        // Save the ICO file
        await sharp(icoBuffer).toFile(icoFilePath);

        console.log(`ICO file saved at ${icoFilePath}`);
    } catch (error) {
        console.error('Error converting PNG to ICO:', error);
    }
}