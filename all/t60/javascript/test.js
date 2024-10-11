describe('findCommonColumns', () => {
  let tempDir;
  let file1Path;
  let file2Path;

  beforeEach(() => {
    // Create a temporary directory for testing
    tempDir = fs.mkdtempSync(path.join(__dirname, 'test-'));

    // Create two sample CSV files with some common and unique columns
    file1Path = path.join(tempDir, 'file1.csv');
    fs.writeFileSync(file1Path, 'col1,col2,col3\na,b,c');

    file2Path = path.join(tempDir, 'file2.csv');
    fs.writeFileSync(file2Path, 'col1,col2,col4\nd,e,f');
  });

  afterEach(() => {
    // Clean up the temporary directory after each test
    fs.rmdirSync(tempDir, { recursive: true });
  });

  test('should find common columns between two CSV files', async () => {
    const result = await findCommonColumns(tempDir);
    expect(result).toEqual(['col1', 'col2']);
  });
});