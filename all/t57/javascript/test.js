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