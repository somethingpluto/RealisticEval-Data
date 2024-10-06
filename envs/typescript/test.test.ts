export function compressFileName(fileName: string, maxLength: number = 18): string {
    if (fileName.length <= maxLength) return fileName;

    const extension = fileName.split('.').pop();
    const baseName = fileName.substring(0, fileName.length - extension.length - 1);
    const ellipsis = '...';
    const allowedLength = maxLength - ellipsis.length - extension.length - 1;

    const startLength = Math.ceil(allowedLength / 2);
    const endLength = Math.floor(allowedLength / 2);

    return `${baseName.slice(0, startLength)}${ellipsis}${baseName.slice(-endLength)}.${extension}`;
}
describe('compressFileName', () => {
    test('returns the original file name if within maxLength', () => {
        // @ts-ignore
        expect(compressFileName('example.txt', 12)).toBe('example.txt');
    });

    test('compresses the file name correctly when it exceeds maxLength', () => {
        // @ts-ignore
        expect(compressFileName('longfilenameexample.txt', 18)).toBe('longf...xample.txt');
    });

    test('handles file names without extension correctly', () => {
        // @ts-ignore
        expect(compressFileName('averylongfilenamewithoutanextension', 20)).toBe('averylon...extension');
    });

    test('returns the original file name when maxLength is larger than file name', () => {
        // @ts-ignore
        expect(compressFileName('short.txt', 20)).toBe('short.txt');
    });

    test('compresses file names with special characters correctly', () => {
        // @ts-ignore
        expect(compressFileName('my$pecialfilename.txt', 18)).toBe('my$pe...lename.txt');
    });
});
