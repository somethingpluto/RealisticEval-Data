/**
 * Converts a given number of Bytes into a readable string representation with the appropriate units (Bytes, KB, MB, GB, or TB) and keeps two decimal places.
 *
 * @param {number} bytes - The number of bytes to be converted.
 * @returns {string} - A string representation of the size in Bytes, KB, MB, GB, or TB.
 */
function bytesToSize(bytes) {
    const units = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    let unitIndex = 0;

    while (bytes >= 1024 && unitIndex < units.length - 1) {
        bytes /= 1024;
        unitIndex++;
    }

    return bytes.toFixed(2) + ' ' + units[unitIndex];
}
describe('bytesToSize', () => {
    test('should convert bytes to KB correctly', () => {
        expect(bytesToSize(1024)).toBe('1.00 KB');
        expect(bytesToSize(2048)).toBe('2.00 KB');
    });

    test('should convert bytes to MB correctly', () => {
        expect(bytesToSize(1048576)).toBe('1.00 MB');
        expect(bytesToSize(2097152)).toBe('2.00 MB');
    });

    test('should convert bytes to GB correctly', () => {
        expect(bytesToSize(1073741824)).toBe('1.00 GB');
        expect(bytesToSize(2147483648)).toBe('2.00 GB');
    });

    test('should convert bytes to TB correctly', () => {
        expect(bytesToSize(1099511627776)).toBe('1.00 TB');
        expect(bytesToSize(2199023255552)).toBe('2.00 TB');
    });
});
