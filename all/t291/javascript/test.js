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