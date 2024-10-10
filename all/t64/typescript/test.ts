describe('CSV to SQL Insert', () => {
  it('should convert CSV content to SQL insert statement', async () => {
    // Mock CSV file content
    const mockCsvContent = `
      id,name,age
      1,Alice,30
      2,Bob,25
    `;

    // Write mock CSV file to disk
    const tempFilePath = '/tmp/temp.csv';
    fs.writeFileSync(tempFilePath, mockCsvContent);

    // Function to simulate reading the CSV file and converting to SQL
    function csvToSqlInsert(filePath: string): Promise<string> {
      return new Promise((resolve, reject) => {
        let sqlStatements = '';
        fs.createReadStream(filePath)
          .pipe(parse({ columns: true }))
          .on('data', (row) => {
            sqlStatements += `INSERT INTO ${filePath.replace('.csv', '')} (${Object.keys(row).join(', ')}) VALUES (${Object.values(row).map(value => `'${value}'`).join(', ')});\n`;
          })
          .on('end', () => resolve(sqlStatements))
          .on('error', (err) => reject(err));
      });
    }

    // Call the function with the temporary file path
    csvToSqlInsert(tempFilePath).then((sql) => {
      expect(sql.trim()).toBe(`
        INSERT INTO /tmp/temp.csv (id, name, age) VALUES ('1', 'Alice', '30');
        INSERT INTO /tmp/temp.csv (id, name, age) VALUES ('2', 'Bob', '25');
      `.trim());
    }).catch((err) => {
      console.error(err);
    });

    // Clean up - remove the temporary file
    fs.unlinkSync(tempFilePath);
  });
});