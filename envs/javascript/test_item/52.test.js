/**
 * Renames a Windows file path by replacing colons in the filename with underscores.
 * 
 * @param {string} path - The original file path.
 * @returns {string} The modified file path with colons in the filename replaced by underscores.
 */
function renameFilePath(path) {
    const parts = path.split('\\');
    const lastPart = parts[parts.length - 1];
    const modifiedLastPart = lastPart.replace(':', '_');
    parts[parts.length - 1] = modifiedLastPart;
    return parts.join('\\');
}
describe('TestRenameFilePath', () => {
  it('should rename a path with colon in the filename', () => {
      // Test path with colon in the filename
      const path = 'C:\\Users\\example\\Documents\\report:2023.txt';
      const expected = 'C:\\Users\\example\\Documents\\report_2023.txt';
      expect(renameFilePath(path)).toEqual(expected);
  });

  it('should not rename a path without colon in the filename', () => {
      // Test path without colon in the filename
      const path = 'C:\\Users\\example\\Documents\\report2023.txt';
      const expected = 'C:\\Users\\example\\Documents\\report2023.txt';
      expect(renameFilePath(path)).toEqual(expected);
  });

  it('should rename a path with multiple colons in the filename', () => {
      // Test path with multiple colons in the filename
      const path = 'C:\\Users\\example\\Documents\\project:report:2023.txt';
      const expected = 'C:\\Users\\example\\Documents\\project_report_2023.txt';
      expect(renameFilePath(path)).toEqual(expected);
  });

  it('should rename a path with a colon at the end of the filename', () => {
      // Test path with a colon at the end of the filename
      const path = 'C:\\Users\\example\\Documents\\backup:';
      const expected = 'C:\\Users\\example\\Documents\\backup_';
      expect(renameFilePath(path)).toEqual(expected);
  });

  it('should rename a path with a colon at the start of the filename', () => {
      // Test path with a colon at the start of the filename
      const path = 'C:\\Users\\example\\Documents\\:initial_setup.txt';
      const expected = 'C:\\Users\\example\\Documents\\_initial_setup.txt';
      expect(renameFilePath(path)).toEqual(expected);
  });
});
