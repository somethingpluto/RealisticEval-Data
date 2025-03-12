const fs = require('fs').promises;
const diff = require('diff');

/**
 * Compare the contents of two files and print the differences in unified diff format.
 *
 * @param {string} file1Path - Path to the first file.
 * @param {string} file2Path - Path to the second file.
 * @returns {Promise<Array<string>>} A promise that resolves to a list containing the lines of differences, if any.
 * @throws {Error} If either file does not exist.
 * @throws {Error} If there is an error reading the files.
 */
async function compareFiles(file1Path, file2Path) {
    try {
        // Read the contents of both files
        const [file1Content, file2Content] = await Promise.all([
            fs.readFile(file1Path, 'utf8'),
            fs.readFile(file2Path, 'utf8')
        ]);

        // Generate the diff
        const differences = diff.createPatch(
            file1Path,
            file1Content,
            file2Content,
            '',
            ''
        );

        // Split the patch into lines
        const diffLines = differences.split('\n').slice(4); // Skip the header lines

        // Filter out any empty lines
        const filteredDiffLines = diffLines.filter(line => line.trim() !== '');

        return filteredDiffLines;
    } catch (error) {
        // Handle errors related to file reading or other issues
        if (error.code === 'ENOENT') {
            throw new Error(`File not found: ${error.path}`);
        } else {
            throw new Error(`Error reading files: ${error.message}`);
        }
    }
}
describe('TestCompareFiles', () => {
  let file1Path;
  let file2Path;

  beforeEach(() => {
      // Create files for testing
      file1Path = 'file1.txt';
      file2Path = 'file2.txt';
  });

  afterEach(() => {
      // Remove created files
      if (fs.existsSync(file1Path)) {
          fs.unlinkSync(file1Path);
      }
      if (fs.existsSync(file2Path)) {
          fs.unlinkSync(file2Path);
      }
  });

  it('should detect no differences in identical files', () => {
      const file1Content = "Line1\nLine2\nLine3\n";
      const file2Content = "Line1\nLine2\nLine3\n";

      fs.writeFileSync(file1Path, file1Content);
      fs.writeFileSync(file2Path, file2Content);

      const result = compareFiles(file1Path, file2Path);
      expect(result.length).toBe(0, "There should be no differences detected");
  });

  it('should detect differences in different files', () => {
      const file1Content = "Line1\nLine2\nLine3\n";
      const file2Content = "Line1\nLineChanged\nLine3\n";

      fs.writeFileSync(file1Path, file1Content);
      fs.writeFileSync(file2Path, file2Content);

      const result = compareFiles(file1Path, file2Path);
      expect(result.length).not.toBe(0, "There should be differences detected");
  });

  it('should throw an error when one of the files does not exist', () => {
      const mockOpen = jest.fn().mockImplementation(() => {
          throw new Error('File not found');
      });

      global.open = mockOpen;

      expect(() => compareFiles('nonexistent.txt', 'file2.txt')).toThrow('One of the files was not found.');

      delete global.open;
  });

  it('should throw an error when there is an error reading the file', () => {
      const mockOpen = jest.fn().mockImplementation(() => {
          throw new Error('Error reading file');
      });

      global.open = mockOpen;

      expect(() => compareFiles('file1.txt', 'file2.txt')).toThrow('Error reading files: Error reading file');

      delete global.open;
  });
});
