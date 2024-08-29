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
