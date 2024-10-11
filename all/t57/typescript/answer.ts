import * as sharp from 'sharp';

interface IconSize {
    width: number;
    height: number;
}

async function convertPngToIco(pngFilePath: string, icoFilePath: string, iconSizes: IconSize[] = [{ width: 32, height: 32 }]): Promise<void> {
    /**
     * Convert PNG images to ICO files
     * @param pngFilePath - Path to the source PNG image file.
     * @param icoFilePath - Path to save the ICO file.
     * @param iconSizes - List of objects specifying the sizes to include in the ICO file.
     */

    try {
        const promises = iconSizes.map(async (size) => {
            await sharp(pngFilePath)
                .resize(size.width, size.height)
                .toFile(`${icoFilePath}_${size.width}x${size.height}.ico`);
        });

        await Promise.all(promises);
        console.log('ICO files generated successfully.');
    } catch (error) {
        console.error('Error converting PNG to ICO:', error);
    }
}