import * as path from 'path';

function renameFilePath(filePath: string): string {
    /**
     * Renames a Windows file path by replacing colons in the filename with underscores.
     * 
     * Parameters:
     *   filePath (string): The original file path.
     * 
     * Returns:
     *   string: The modified file path with colons in the filename replaced by underscores.
     */

    // Split the path into directory and filename
    const directory = path.dirname(filePath);
    const filename = path.basename(filePath);

    // Replace colons in the filename with underscores
    const sanitizedFilename = filename.replace(/:/g, '_');

    // Reconstruct the full path with the sanitized filename
    const newPath = path.join(directory, sanitizedFilename);

    return newPath;
}

// Example usage:
// const result = renameFilePath('C:\\example\\file:name.txt');
// console.log(result); // Output: 'C:\\example\\file_name.txt'