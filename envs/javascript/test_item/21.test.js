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
  const fs = require('fs').promises;
  const path = require('path');

  // Check if both files exist
  try {
    await fs.access(file1Path);
    await fs.access(file2Path);
  } catch (error) {
    throw new Error('One or both files do not exist.');
  }

  try {
    // Read the contents of both files
    const file1Content = await fs.readFile(file1Path, 'utf8');
    const file2Content = await fs.readFile(file2Path, 'utf8');

    // Split the contents into lines
    const file1Lines = file1Content.split('\n');
    const file2Lines = file2Content.split('\n');

    // Compare the lines and generate the diff
    const diff = [];
    let lineNum = 1;
    let file1Index = 0, file2Index = 0;

    while (file1Index < file1Lines.length || file2Index < file2Lines.length) {
      if (file1Index < file1Lines.length && file2Index < file2Lines.length && file1Lines[file1Index] === file2Lines[file2Index]) {
        // Lines are the same
        diff.push(`@@ -${lineNum},${file1Lines.length - lineNum + 1} +${lineNum},${file2Lines.length - lineNum + 1} @@`);
        diff.push(` ${file1Lines[file1Index]}`);
        lineNum++;
        file1Index++;
        file2Index++;
      } else if (file1Index < file1Lines.length && (file2Index >= file2Lines.length || file1Lines[file1Index] !== file2Lines[file2Index])) {
        // Line exists in file1 but not in file2
        diff.push(`@@ -${lineNum},${file1Lines.length - lineNum + 1} +${lineNum},${file2Lines.length - lineNum + 1} @@`);
        diff.push(`-${file1Lines[file1Index]}`);
        lineNum++;
        file1Index++;
      } else if (file2Index < file2Lines.length && (file1Index >= file1Lines.length || file1Lines[file1Index] !== file2Lines[file2Index])) {
        // Line exists in file2 but not in file1
        diff.push(`@@ -${lineNum},${file1Lines.length - lineNum + 1} +${lineNum},${file2Lines.length - lineNum + 1} @@`);
        diff.push(`+${file2Lines[file2Index]}`);
        lineNum++;
        file2Index++;
      }
    }

    return diff;
  } catch (error) {
    throw new Error('Error reading the files.');
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
