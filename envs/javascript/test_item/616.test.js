/**
 * Converts a size in bytes to a human-readable string representation.
 *
 * @param {number} sizeInBytes - The size in bytes to convert.
 * @returns {string} A string representation of the size in an appropriate unit (bytes, KB, MB, GB, TB).
 */
function byteCountToDisplaySize(sizeInBytes) {
    if (isNaN(sizeInBytes) || sizeInBytes < 0) {
        return 'Invalid size';
    }

    const units = ['bytes', 'KB', 'MB', 'GB', 'TB'];
    let unitIndex = 0;

    while (sizeInBytes >= 1024 && unitIndex < units.length - 1) {
        sizeInBytes /= 1024;
        unitIndex++;
    }

    return `${sizeInBytes.toFixed(2)} ${units[unitIndex]}`;
}
describe('byteCountToDisplaySize', () => {
    test('should return "0 bytes" for 0 bytes', () => {
        const inputSize = 0;
        const expected = "0 bytes";
        expect(byteCountToDisplaySize(inputSize)).toBe(expected);
    });

    test('should return "500 bytes" for 500 bytes', () => {
        const inputSize = 500;
        const expected = "500 bytes";
        expect(byteCountToDisplaySize(inputSize)).toBe(expected);
    });

    test('should return "1 KB" or "1.00 KB" for exactly 1 KB', () => {
        const inputSize = 1024;
        const result = byteCountToDisplaySize(inputSize);
        expect(result).toMatch(/1 KB|1\.00 KB/);
    });

    test('should return "4.88 KB" for a size between 1 KB and 1 MB', () => {
        const inputSize = 5000;
        const expected = "4.88 KB";
        expect(byteCountToDisplaySize(inputSize)).toBe(expected);
    });

    test('should return "1 MB" or "1.00 MB" for exactly 1 MB', () => {
        const inputSize = 1048576; // 1024 * 1024
        const result = byteCountToDisplaySize(inputSize);
        expect(result).toMatch(/1 MB|1\.00 MB/);
    });
});
