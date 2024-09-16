/**
 * Compresses long filenames to the specified maximum length by inserting an ellipsis in the middle while preserving the filename extension, which defaults to 18 characters
 *
 * @param {string} fileName - The original file name to be compressed.
 * @param {number} maxLength - The maximum allowed length for the compressed file name. Defaults to 18.
 * @returns {string} The compressed file name, with the middle section replaced by ellipses ('...'), or the original file name if it is within the maximum length.
 */
export function compressFileName(
  fileName: string,
  maxLength: number = 18
): string {
  if (fileName.length <= maxLength) {
    return fileName.trim();
  }

  let extensionIndex = fileName.lastIndexOf('.');
  if (extensionIndex==-1) extensionIndex = fileName.length;
  const fileNameWithoutExtension = fileName.substring(0, extensionIndex);
  const fileExtension = fileName.substring(extensionIndex);

  const availableLength = maxLength - fileExtension.length - 3;
  const startLength = Math.floor(availableLength / 2);
  const endLength = availableLength - startLength;

  const compressedFileName =
    fileNameWithoutExtension.substring(0, startLength) +
    '...' +
    fileNameWithoutExtension.substring(fileNameWithoutExtension.length - endLength) +
    fileExtension;

  return compressedFileName;
}