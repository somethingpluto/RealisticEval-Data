const path = require('path');

/**
 * Renames a Windows file path by replacing colons in the filename with underscores.
 *
 * @param {string} path - The original file path.
 * @returns {string} The modified file path with colons in the filename replaced by underscores.
 */
function renameFilePath(path) {

    // Split the path into directory and filename
    const [directory, filename] = path.parse(path);
    
    // Replace colons in the filename with underscores
    const sanitizedFilename = filename.replace(/:/g, '_');
    
    // Reconstruct the full path with the sanitized filename
    const newPath = path.format({ dir: directory, base: sanitizedFilename });
    
    return newPath;
}