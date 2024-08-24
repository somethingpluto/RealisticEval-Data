describe('bytesToSize', () => {
    test('should return "0 Byte" for 0 bytes', () => {
        // @ts-ignore
        expect(bytesToSize(0)).toBe('0 Byte');
    });

    test('should convert bytes to KB correctly', () => {
        // @ts-ignore
        expect(bytesToSize(1024)).toBe('1.00 KB');
        // @ts-ignore
        expect(bytesToSize(2048)).toBe('2.00 KB');
    });

    test('should convert bytes to MB correctly', () => {
        // @ts-ignore
        expect(bytesToSize(1048576)).toBe('1.00 MB');
        // @ts-ignore
        expect(bytesToSize(2097152)).toBe('2.00 MB');
    });

    test('should convert bytes to GB correctly', () => {
        // @ts-ignore
        expect(bytesToSize(1073741824)).toBe('1.00 GB');
        // @ts-ignore
        expect(bytesToSize(2147483648)).toBe('2.00 GB');
    });

    test('should convert bytes to TB correctly', () => {
        // @ts-ignore
        expect(bytesToSize(1099511627776)).toBe('1.00 TB');
        // @ts-ignore
        expect(bytesToSize(2199023255552)).toBe('2.00 TB');
    });
});

/**
 * Converts a given number of Bytes into a readable string representation with the appropriate units (Bytes, KB, MB, GB, or TB) and keeps two decimal places *
 *
 * @param {number} bytes - The number of bytes to be converted.
 * @returns {string} - A string representation of the size in Bytes, KB, MB, GB, or TB.
 */
export function bytesToSize(bytes: number): string {
    // Define the size units array
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];

    // Return '0 Byte' if the input is zero
    if (bytes === 0) return '0 Byte';

    // Calculate the index for the size unit and the converted size
    const i = Math.floor(Math.log(bytes) / Math.log(1024));
    const size = (bytes / Math.pow(1024, i)).toFixed(2);

    // Return the size with the appropriate unit
    return `${size} ${sizes[i]}`;
}
