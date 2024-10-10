describe('compareFiles function', () => {
    const file1Path = 'path/to/file1.txt';
    const file2Path = 'path/to/file2.txt';
  
    beforeEach(() => {
      fs.readFileSync.mockReset();
    });
  
    test('should return an empty array if both files are identical', () => {
      const content1 = 'Hello World\nThis is a test.\nEnd of file.';
      const content2 = 'Hello World\nThis is a test.\nEnd of file.';
  
      fs.readFileSync.mockImplementation((filePath) => {
        if (filePath === file1Path) return content1;
        if (filePath === file2Path) return content2;
        throw new Error(`File not found: ${filePath}`);
      });
  
      expect(compareFiles(file1Path, file2Path)).toEqual([]);
    });
  
    test('should return differences if files are different', () => {
      const content1 = 'Hello World\nThis is a test.\nEnd of file.';
      const content2 = 'Hello World\nThis is a different test.\nEnd of file.';
  
      fs.readFileSync.mockImplementation((filePath) => {
        if (filePath === file1Path) return content1;
        if (filePath === file2Path) return content2;
        throw new Error(`File not found: ${filePath}`);
      });
  
      expect(compareFiles(file1Path, file2Path)).toEqual([
        '- This is a test.',
        '+ This is a different test.',
      ]);
    });
  
    test('should throw an error if file1 does not exist', () => {
      fs.readFileSync.mockImplementationOnce((filePath) => {
        if (filePath === file1Path) throw new Error(`File not found: ${file1Path}`);
        if (filePath === file2Path) return 'Some content';
        throw new Error(`File not found: ${filePath}`);
      });
  
      expect(() => compareFiles(file1Path, file2Path)).toThrowError(/File not found/);
    });
  
    test('should throw an error if file2 does not exist', () => {
      fs.readFileSync.mockImplementationOnce((filePath) => {
        if (filePath === file1Path) return 'Some content';
        if (filePath === file2Path) throw new Error(`File not found: ${file2Path}`);
        throw new Error(`File not found: ${filePath}`);
      });
  
      expect(() => compareFiles(file1Path, file2Path)).toThrowError(/File not found/);
    });
  });