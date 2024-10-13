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