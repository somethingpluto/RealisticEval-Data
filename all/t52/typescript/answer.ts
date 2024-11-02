import path from "path";

/**
 * Renames a Windows file path by replacing colons in the filename with underscores.
 *
 * @param {string} filePath - The original file path.
 * @returns {string} - The modified file path with colons in the filename replaced by underscores.
 */
function renameFilePath(filePath: string): string {
    // Parse the file path to get directory and filename
    const { dir, base } = path.parse(filePath);

    // Replace colons in the filename with underscores
    const sanitizedFilename = base.replace(/:/g, '_');

    // Reconstruct the full path with the sanitized filename
    const newPath = path.join(dir, sanitizedFilename);

    return newPath;
}