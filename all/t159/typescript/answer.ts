/**
 * Removes the extension of the given filename and returns the remainder
 *
 * @param {string} file_name - The full name of the file from which to remove the extension.
 * @returns {string} The file name without the extension. If no extension is found, returns the original file name.
 */
function removeFileExtension(file_name: string): string {
    // Find the index of the last dot in the file name
    const lastDotIndex = file_name.lastIndexOf('.');

    // If a dot is found and it is not the first character
    if (lastDotIndex !== -1) {
        // Return the substring from the beginning to the last dot
        return file_name.slice(0, lastDotIndex);
    }

    // Return the original file name if no dot is found
    return file_name;
}
