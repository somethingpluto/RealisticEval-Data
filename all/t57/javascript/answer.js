const sharp = require('sharp');
const fs = require('fs');

function convertPngToIco(pngFilePath, icoFilePath, iconSizes = [[32, 32]]) {
    /**
     * Convert PNG images to ICO files
     * @param {string} pngFilePath - Path to the source PNG image file.
     * @param {string} icoFilePath - Path to save the ICO file.
     * @param {Array<Array<number>>} iconSizes - Array of arrays specifying the sizes to include in the ICO file.
     */

    Promise.all(iconSizes.map(([width, height]) =>
        sharp(pngFilePath)
            .resize(width, height)
            .png()
            .toBuffer()
    ))
    .then(buffers => {
        const buffer = Buffer.concat(buffers);

        // Create ICO header and write it to the file
        let icoHeader = Buffer.alloc(6);
        icoHeader.writeUInt16LE(0x4D42); // BM for bitmap
        icoHeader.writeUInt32LE(buffer.length + 6 + iconSizes.length * 16, 2);

        // Create ICO directory entries
        let dirEntries = [];
        let offset = 6 + iconSizes.length * 16;
        iconSizes.forEach(([width, height], index) => {
            let entry = Buffer.alloc(16);
            entry.writeUInt8(0, 0); // Reserved
            entry.writeUInt8(0, 1); // Color planes
            entry.writeUInt16LE(0, 2); // Bits per pixel
            entry.writeUInt32LE(buffer.length, 4); // Size of image data
            entry.writeUInt32LE(offset, 8); // Offset of image data
            entry.writeUInt16LE(height, 12); // Image height
            entry.writeUInt16LE(width, 14); // Image width

            dirEntries.push(entry);
            offset += buffer.length;
        });

        // Write all buffers to the output file
        const icoFile = Buffer.concat([icoHeader, ...dirEntries, buffer]);
        fs.writeFileSync(icoFilePath, icoFile);
    })
    .catch(err => console.error('Error converting image:', err));
}
