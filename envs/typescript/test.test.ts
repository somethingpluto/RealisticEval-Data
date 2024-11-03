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
import { mock } from 'jest-mock-extended';

describe('TestConvertPngToIco', () => {
    let mockImage: any;

    beforeEach(() => {
        mockImage = mock();
    });

    describe('convertPngToIco', () => {
        it('should save ICO with a single icon size', () => {
            const mockOpen = jest.fn().mockReturnValue({
                __enter__: jest.fn().mockReturnValue(mockImage),
                __exit__: jest.fn(),
            });

            jest.spyOn(global, 'Image').mockImplementation(() => ({
                open: mockOpen,
            }));

            convertPngToIco('source.png', 'output.ico', [[64, 64]]);
            expect(mockImage.save).toHaveBeenCalledWith('output.ico', { format: 'ICO', sizes: [[64, 64]] });
        });

        it('should save ICO with multiple icon sizes', () => {
            const mockOpen = jest.fn().mockReturnValue({
                __enter__: jest.fn().mockReturnValue(mockImage),
                __exit__: jest.fn(),
            });

            jest.spyOn(global, 'Image').mockImplementation(() => ({
                open: mockOpen,
            }));

            convertPngToIco('source.png', 'output.ico', [[16, 16], [32, 32], [64, 64]]);
            expect(mockImage.save).toHaveBeenCalledWith('output.ico', { format: 'ICO', sizes: [[16, 16], [32, 32], [64, 64]] });
        });

        it('should save ICO with the default icon size', () => {
            const mockOpen = jest.fn().mockReturnValue({
                __enter__: jest.fn().mockReturnValue(mockImage),
                __exit__: jest.fn(),
            });

            jest.spyOn(global, 'Image').mockImplementation(() => ({
                open: mockOpen,
            }));

            convertPngToIco('source.png', 'output.ico');
            expect(mockImage.save).toHaveBeenCalledWith('output.ico', { format: 'ICO', sizes: [[32, 32]] });
        });

        it('should handle file opening correctly', () => {
            const mockOpen = jest.fn().mockReturnValue({
                __enter__: jest.fn().mockReturnValue(mockImage),
                __exit__: jest.fn(),
            });

            jest.spyOn(global, 'Image').mockImplementation(() => ({
                open: mockOpen,
            }));

            convertPngToIco('source.png', 'output.ico');
            expect(mockImage.save).toHaveBeenCalledTimes(1);
            expect(mockImage.save).toHaveBeenCalledWith('output.ico', { format: 'ICO', sizes: [[32, 32]] });
        });

        it('should throw an error when the image path is invalid', () => {
            const mockOpen = jest.fn().mockImplementation(() => {
                throw new Error('File not found');
            });

            jest.spyOn(global, 'Image').mockImplementation(() => ({
                open: mockOpen,
            }));

            expect(() => convertPngToIco('invalid.png', 'output.ico')).toThrow('File not found');
        });
    });
});
