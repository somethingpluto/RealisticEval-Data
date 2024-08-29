/**
 * Compresses long filenames to the specified maximum length by inserting an ellipsis in the middle while preserving the filename extension, which defaults to 18 characters
 *
 * @param {string} fileName - The original file name to be compressed.
 * @param {number} maxLength - The maximum allowed length for the compressed file name. Defaults to 18.
 * @returns {string} The compressed file name, with the middle section replaced by ellipses ('...'), or the original file name if it is within the maximum length.
 */
// @ts-ignore
export function compressFileName(fileName: string, maxLength: number = 18): string {

}