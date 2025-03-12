const fs = require('fs').promises;

/**
 * Appends the specified string to the beginning of each line of the file.
 * 
 * @param {string} file_path - Path to the file whose lines will be modified.
 * @param {string} prefix - String to append to the beginning of each line.
 */
async function prependToEachLine(file_path, prefix) {
    try {
        // Read the file content
        let fileContent = await fs.readFile(file_path, 'utf8');
        
        // Split the content into lines
        let lines = fileContent.split('\n');
        
        // Prepend the prefix to each line
        let modifiedLines = lines.map(line => prefix + line);
        
        // Join the lines back into a single string
        let modifiedContent = modifiedLines.join('\n');
        
        // Write the modified content back to the file
        await fs.writeFile(file_path, modifiedContent, 'utf8');
        
    } catch (error) {
        console.error('Error occurred while processing the file:', error);
    }
}
const fs = require('fs').promises;
const os = require('os');
describe('TestPrependToEachLine', () => {
  let testFilePath;

  beforeAll(() => {
      testFilePath = 'test_file.txt';
      return fs.writeFile(testFilePath, 'Line 1\nLine 2\nLine 3');
  });

  afterAll(() => {
      return fs.unlink(testFilePath);
  });

  it('should prepend a simple string to each line', async () => {
      await prependToEachLine(testFilePath, 'Test: ');
      const content = await fs.readFile(testFilePath, 'utf8');
      const lines = content.split(os.EOL);
      expect(lines).toEqual(['Test: Line 1', 'Test: Line 2', 'Test: Line 3']);
  });

  it('should prepend an empty string', async () => {
      await prependToEachLine(testFilePath, '');
      const content = await fs.readFile(testFilePath, 'utf8');
      const lines = content.split(os.EOL);
      expect(lines).toEqual(['Line 1', 'Line 2', 'Line 3']);
  });

  it('should prepend special characters to each line', async () => {
      await prependToEachLine(testFilePath, '#$%^&* ');
      const content = await fs.readFile(testFilePath, 'utf8');
      const lines = content.split(os.EOL);
      expect(lines).toEqual(['#$%^&* Line 1', '#$%^&* Line 2', '#$%^&* Line 3']);
  });

  it('should prepend a numeric string to each line', async () => {
      await prependToEachLine(testFilePath, '123 ');
      const content = await fs.readFile(testFilePath, 'utf8');
      const lines = content.split(os.EOL);
      expect(lines).toEqual(['123 Line 1', '123 Line 2', '123 Line 3']);
  });

  it('should throw an error if the file does not exist', async () => {
      await expect(prependToEachLine('non_existent_file.txt', 'Test: '))
          .rejects.toThrowError(/ENOENT/);
  });
});
