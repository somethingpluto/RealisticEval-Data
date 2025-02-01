const fs = require('fs');
const path = require('path');
const csvParser = require('csv-parser');

/**
 * Converts the contents of a CSV file into an SQL insert statement with a table name with the suffix removed.
 * 
 * @param {string} csvFilePath - The path to the CSV file.
 * @returns {Promise<string>} A promise that resolves to the parsed SQL insert statements.
 */
function csvToSqlInsert(csvFilePath) {
  return new Promise((resolve, reject) => {
    const results = [];
    const tableName = path.parse(csvFilePath).name; // Get the table name without the extension and suffix
    const sqlInserts = [];

    fs.createReadStream(csvFilePath)
      .pipe(csvParser())
      .on('data', (data) => results.push(data))
      .on('end', () => {
        const columns = Object.keys(results[0]).join(', ');
        results.forEach((row) => {
          const values = Object.values(row).map((value) => `'${value}'`).join(', ');
          sqlInserts.push(`INSERT INTO ${tableName} (${columns}) VALUES (${values});`);
        });
        resolve(sqlInserts.join('\n'));
      })
      .on('error', (error) => {
        reject(error);
      });
  });
}

// Example usage:
// csvToSqlInsert('path/to/your/file.csv')
//   .then((sqlInserts) => {
//     console.log(sqlInserts);
//   })
//   .catch((error) => {
//     console.error('Error:', error);
//   });
const fs = require('fs');
const path = require('path');
const csvParser = require('csv-parser');

describe('TestCsvToSqlInsert', () => {
  beforeAll(() => {
      // Create sample CSV files for testing
      const testFiles = {
          'test1.csv': 'id,name,age\n1,Alice,30\n2,Bob,25',
          'test2.csv': 'product_id,product_name,price\n101,Widget,9.99\n102,Gadget,12.49',
          'test3.csv': 'user_id,email\n3,test@example.com\n4,user@domain.com',
          'test4.csv': 'order_id,order_date,total\n1001,2024-09-01,59.99',
          'test5.csv': 'quote_id,quote\n1,"It\'s a beautiful day."\n2,"She said, ""Hello!"""'
      };

      // Create the files on disk
      for (const [filename, content] of Object.entries(testFiles)) {
          fs.writeFileSync(filename, content);
      }
  });

  afterAll(() => {
      // Remove the test files after tests
      const testFiles = Object.keys(testFiles);
      testFiles.forEach(filename => fs.unlinkSync(filename));
  });

  it('should handle simple CSV correctly', () => {
      const expectedSql = (
          "INSERT INTO test1 (id, name, age) VALUES ('1', 'Alice', '30');\n" +
          "INSERT INTO test1 (id, name, age) VALUES ('2', 'Bob', '25');"
      );
      const result = csv_to_sql_insert('test1.csv');
      expect(result).toEqual(expectedSql);
  });

  it('should handle product CSV correctly', () => {
      const expectedSql = (
          "INSERT INTO test2 (product_id, product_name, price) VALUES ('101', 'Widget', '9.99');\n" +
          "INSERT INTO test2 (product_id, product_name, price) VALUES ('102', 'Gadget', '12.49');"
      );
      const result = csv_to_sql_insert('test2.csv');
      expect(result).toEqual(expectedSql);
  });

  it('should handle email CSV correctly', () => {
      const expectedSql = (
          "INSERT INTO test3 (user_id, email) VALUES ('3', 'test@example.com');\n" +
          "INSERT INTO test3 (user_id, email) VALUES ('4', 'user@domain.com');"
      );
      const result = csv_to_sql_insert('test4.csv');
      expect(result).toEqual(expectedSql);
  });

  it('should handle date and decimal CSV correctly', () => {
      const expectedSql = (
          "INSERT INTO test4 (order_id, order_date, total) VALUES ('1001', '2024-09-01', '59.99');"
      );
      const result = csv_to_sql_insert('test4.csv');
      expect(result).toEqual(expectedSql);
  });
});
