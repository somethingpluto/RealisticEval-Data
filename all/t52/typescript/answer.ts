function renameFilePath(path: string): string {
    /**
     * Renames a Windows file path by replacing colons in the filename with underscores.
     *
     * @param {string} path - The original file path.
     * @returns {string} - The modified file path with colons in the filename replaced by underscores.
     */
    // Split the path into directory and filename
    const [directory, filename] = path.parse(path).dir.split(path.sep).pop() + path.parse(path).base;

    // Replace colons in the filename with underscores
    const sanitizedFilename = filename.replace(/:/g, '_');

    // Reconstruct the full path with the sanitized filename
    const newPath = path.join(directory, sanitizedFilename);

    return newPath;
}