import sharp from 'sharp'; // Assuming sharp is installed and can handle image conversions

interface IconSizes {
    width: number;
    height: number;
}

/**
 * Convert a PNG image file to an ICO format file.
 *
 * @param pngFilePath - Path to the source PNG image file.
 * @param icoFilePath - Path to save the ICO file.
 * @param iconSizes - List of tuples specifying the sizes to include in the ICO file.
 */
function convertPngToIco(pngFilePath: string, icoFilePath: string, iconSizes: IconSizes[] = [{ width: 32, height: 32 }]): void {
    // Open the image file using sharp
    sharp(pngFilePath)
        .resize(iconSizes[0].width, iconSizes[0].height)
        .toFile(icoFilePath, (err, info) => {
            if (err) {
                console.error('Error converting PNG to ICO:', err);
            } else {
                console.log('ICO file saved successfully:', icoFilePath);
            }
        });
}