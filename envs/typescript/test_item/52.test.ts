import { promises as fs } from 'fs';

/**
 * Renames a Windows file path by replacing colons in the filename with underscores.
 * 
 * @param {string} path - The original file path.
 * @returns {Promise<string>} - A promise that resolves with the modified file path.
 */
async function renameFilePath(path: string): Promise<string> {
    // ... existing code ...
    try {
        const parts = path.split('\\');
        const filename = parts.pop()!;
        const newFilename = filename.replace(/:/g, '_');
        const newPath = parts.concat(newFilename).join('\\');
        await fs.rename(path, newPath);
        return newPath;
    } catch (error) {
        throw new Error(`Failed to rename file: ${error.message}`);
    }
}
describe('TestRenameFilePath', () => {
  it('should rename with colon in the filename', () => {
    // Test path with colon in the filename
    const path = 'C:\\Users\\example\\Documents\\report:2023.txt';
    const expected = 'C:\\Users\\example\\Documents\\report_2023.txt';
    expect(renameFilePath(path)).toEqual(expected);
  });

  it('should rename without colon in the filename', () => {
    // Test path without colon in the filename
    const path = 'C:\\Users\\example\\Documents\\report2023.txt';
    const expected = 'C:\\Users\\example\\Documents\\report2023.txt';
    expect(renameFilePath(path)).toEqual(expected);
  });

  it('should rename with multiple colons in the filename', () => {
    // Test path with multiple colons in the filename
    const path = 'C:\\Users\\example\\Documents\\project:report:2023.txt';
    const expected = 'C:\\Users\\example\\Documents\\project_report_2023.txt';
    expect(renameFilePath(path)).toEqual(expected);
  });

  it('should rename with colon at the end of the filename', () => {
    // Test path with a colon at the end of the filename
    const path = 'C:\\Users\\example\\Documents\\backup:';
    const expected = 'C:\\Users\\example\\Documents\\backup_';
    expect(renameFilePath(path)).toEqual(expected);
  });

  it('should rename with colon at the start of the filename', () => {
    // Test path with a colon at the start of the filename
    const path = 'C:\\Users\\example\\Documents\\:initial_setup.txt';
    const expected = 'C:\\Users\\example\\Documents\\_initial_setup.txt';
    expect(renameFilePath(path)).toEqual(expected);
  });
});
