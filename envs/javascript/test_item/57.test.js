const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

/**
 * Converts a PNG image file to an ICO format file.
 * 
 * @param {string} pngFilePath - Path to the source PNG image file.
 * @param {string} icoFilePath - Path to save the ICO file.
 * @param {Array.<Array.<number>>} [iconSizes=[[32, 32]]] - List of tuples specifying the sizes to include in the ICO file.
 */
async function convertPngToIco(pngFilePath, icoFilePath, iconSizes = [[32, 32]]) {
    try {
        // Validate input paths
        if (!fs.existsSync(pngFilePath)) {
            throw new Error(`Source PNG file does not exist: ${pngFilePath}`);
        }

        // Ensure the output directory exists
        const outputDir = path.dirname(icoFilePath);
        if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // Create an array to hold the resized images
        const resizedImages = [];

        // Resize the PNG image to each specified size and convert to buffer
        for (const [width, height] of iconSizes) {
            const resizedImage = await sharp(pngFilePath)
                .resize(width, height)
                .toBuffer();
            resizedImages.push(resizedImage);
        }

        // Create the ICO file from the resized images
        await sharp(resizedImages[0], {
            raw: {
                width: iconSizes[0][0],
                height: iconSizes[0][1],
                channels: 4
            }
        })
        .toFormat('ico', {
            sizes: iconSizes.map(([width, height]) => ({ width, height }))
        })
        .toFile(icoFilePath);

        console.log(`ICO file created successfully at: ${icoFilePath}`);
    } catch (error) {
        console.error(`Error converting PNG to ICO: ${error.message}`);
    }
}
const fs = require('fs').promises; // Import fs.promises for mocking errors

describe('TestConvertPngToIco', () => {
    beforeEach(() => {
        jest.resetModules();
        jest.clearAllMocks();
    });

    describe('testSingleIconSize', () => {
        it('should save the image with a single icon size', () => {
            const mockImage = {
                save: jest.fn()
            };

            const mockOpen = jest.fn().mockReturnValue({
                __enter__: jest.fn().mockReturnValue(mockImage),
                __exit__: jest.fn()
            });

            jest.doMock('sharp', () => ({
                open: mockOpen
            }));

            convertPngToIco('source.png', 'output.ico', [[64, 64]]);
            expect(mockImage.save).toHaveBeenCalledWith('output.ico', { format: 'ICO', sizes: [[64, 64]] });
        });
    });

    describe('testMultipleIconSizes', () => {
        it('should save the image with multiple icon sizes', () => {
            const mockImage = {
                save: jest.fn()
            };

            const mockOpen = jest.fn().mockReturnValue({
                __enter__: jest.fn().mockReturnValue(mockImage),
                __exit__: jest.fn()
            });

            jest.doMock('sharp', () => ({
                open: mockOpen
            }));

            convertPngToIco('source.png', 'output.ico', [[16, 16], [32, 32], [64, 64]]);
            expect(mockImage.save).toHaveBeenCalledWith('output.ico', { format: 'ICO', sizes: [[16, 16], [32, 32], [64, 64]] });
        });
    });

    describe('testDefaultIconSize', () => {
        it('should save the image with the default icon size', () => {
            const mockImage = {
                save: jest.fn()
            };

            const mockOpen = jest.fn().mockReturnValue({
                __enter__: jest.fn().mockReturnValue(mockImage),
                __exit__: jest.fn()
            });

            jest.doMock('sharp', () => ({
                open: mockOpen
            }));

            convertPngToIco('source.png', 'output.ico');
            expect(mockImage.save).toHaveBeenCalledWith('output.ico', { format: 'ICO', sizes: [[32, 32]] });
        });
    });

    describe('testFileHandling', () => {
        it('should save the image with the correct parameters', () => {
            const mockImage = {
                save: jest.fn()
            };

            const mockOpen = jest.fn().mockReturnValue({
                __enter__: jest.fn().mockReturnValue(mockImage),
                __exit__: jest.fn()
            });

            jest.doMock('sharp', () => ({
                open: mockOpen
            }));

            convertPngToIco('source.png', 'output.ico');
            expect(mockImage.save).toHaveBeenCalledTimes(1);
            expect(mockImage.save).toHaveBeenCalledWith('output.ico', { format: 'ICO', sizes: [[32, 32]] });
        });
    });

    describe('testInvalidImagePath', () => {
        it('should throw an error when the image path is invalid', async () => {
            const mockOpen = jest.fn().mockRejectedValue(new Error('File not found'));

            jest.doMock('sharp', () => ({
                open: mockOpen
            }));

            await expect(convertPngToIco('invalid.png', 'output.ico')).rejects.toThrow('File not found');
        });
    });
});
