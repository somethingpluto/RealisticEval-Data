describe('csv_to_sql_insert', () => {
  afterEach(() => {
    // Clear all instances and calls to constructor and all methods:
    fs.readFileSync.mockClear();
  });

  it('should convert CSV content to SQL insert statement', () => {
    const csvFilePath = 'path/to/your/csvfile.csv';
    const expectedSql = "INSERT INTO tablename (column1, column2) VALUES ('value1', 'value2');";

    // Mock the return value of fs.readFileSync
    fs.readFileSync.mockReturnValueOnce(`
      column1,column2\n
      value1,value2
    `);

    // Call the function with the mocked CSV file path
    const result = csv_to_sql_insert(csvFilePath);

    // Check if the returned SQL statement matches the expected one
    expect(result).toBe(expectedSql);
  });

  it('should handle empty CSV file gracefully', () => {
    const csvFilePath = 'path/to/your/csvfile.csv';
    const expectedSql = "";

    // Mock the return value of fs.readFileSync to represent an empty file
    fs.readFileSync.mockReturnValueOnce('');

    // Call the function with the mocked CSV file path
    const result = csv_to_sql_insert(csvFilePath);

    // Check if the returned SQL statement is an empty string
    expect(result).toBe(expectedSql);
  });
});