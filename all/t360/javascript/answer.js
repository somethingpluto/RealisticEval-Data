/**
 * @brief Extracts the last part of a complete file path with the help of a separator and returns it,
 * or the original string if no separator is found.
 *
 * This function extracts the last part of a file path after the last occurrence of the specified separator.
 * If the separator is not found in the path, the function returns the original string.
 *
 * @param {string} filePath - The complete file path as a string.
 * @return {string} - The last part of the file path after the last separator, 
 * or the original string if no separator is found.
 */
function getLastPartOfFilepath(filePath) {
    const pos = Math.max(filePath.lastIndexOf('/'), filePath.lastIndexOf('\\'));
    if (pos === -1) {
        return filePath; // Return the original string if no separator is found
    }
    return filePath.substring(pos + 1);
}