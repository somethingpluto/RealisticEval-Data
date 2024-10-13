describe('TestCompareFiles', () => {
  let file1Path: string;
  let file2Path: string;

  beforeEach(() => {
    // Create files for testing
    file1Path = 'file1.txt';
    file2Path = 'file2.txt';
  });

  afterEach(() => {
    // Delete created files
    if (fs.existsSync(file1Path)) {
      fs.unlinkSync(file1Path);
    }
    if (fs.existsSync(file2Path)) {
      fs.unlinkSync(file2Path);
    }
  });

  it('should handle identical files correctly', () => {
    const file1Content = "Line1\nLine2\nLine3\n";
    const file2Content = "Line1\nLine2\nLine3\n";

    fs.writeFileSync(file1Path, file1Content);
    fs.writeFileSync(file2Path, file2Content);

    const result = compareFiles(file1Path, file2Path);
    expect(result.length).toBe(0);
  });

  it('should detect differences between files', () => {
    const file1Content = "Line1\nLine2\nLine3\n";
    const file2Content = "Line1\nLineChanged\nLine3\n";

    fs.writeFileSync(file1Path, file1Content);
    fs.writeFileSync(file2Path, file2Content);

    const result = compareFiles(file1Path, file2Path);
    expect(result.length).not.toBe(0);
  });

  it('should throw an error when one of the files does not exist', () => {
    jest.spyOn(fs, 'readFileSync').mockImplementation(() => {
      throw new Error('File not found');
    });

    expect(() => compareFiles('nonexistent.txt', file2Path)).toThrow('File not found');
  });

  it('should throw an error when there is an error reading the file', () => {
    jest.spyOn(fs, 'readFileSync').mockImplementation(() => {
      throw new Error('Error reading file');
    });

    expect(() => compareFiles(file1Path, file2Path)).toThrow('Error reading file');
  });
});