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