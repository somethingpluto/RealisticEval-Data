import path from 'path';

/**
 * Renames a Windows file path by replacing colons in the filename with underscores.
 *
 * @param {string} filePath - The original file path.
 * @returns {string} The modified file path with colons in the filename replaced by underscores.
 */
function renameFilePath(filePath) {
    // Get the directory and filename from the path
    const directory = path.dirname(filePath);
    const filename = path.basename(filePath);
    
    // Replace colons in the filename with underscores
    const sanitizedFilename = filename.replace(/:/g, '_');
    
    // Reconstruct the full path with the sanitized filename
    const newPath = path.join(directory, sanitizedFilename);
    
    return newPath;
}
