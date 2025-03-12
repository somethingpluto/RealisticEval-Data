import * as fs from 'fs';
import * as path from 'path';
import * as csvParser from 'csv-parser';
import { promisify } from 'util';
import { Pool } from 'pg';

const readFileAsync = promisify(fs.readFile);
const pool = new Pool();

async function csvToSqlInsert(csvFilePath: string, tableName: string): Promise<void> {
  try {
    const data = await readFileAsync(csvFilePath, 'utf8');
    const records = data.split('\n').map(line => line.split(','));
    const columns = records.shift().map((_, index) => `column${index + 1}`);
    const values = records.map(record => record.map(value => `'${value.replace(/'/g, "''")}'`).join(', '));
    const insertQuery = `INSERT INTO ${tableName} (${columns.join(', ')}) VALUES ${values.join(', ')};`;

    await pool.query(insertQuery);
  } catch (error) {
    console.error('Error executing SQL insert:', error);
  }
}

export { csvToSqlInsert };
import * as fs from 'fs';
import * as path from 'path';
import * as csvParser from 'csv-parser';


describe('TestCsvToSqlInsert', () => {
  const testFiles = {
      'test1.csv': 'id,name,age\n1,Alice,30\n2,Bob,25',
      'test2.csv': 'product_id,product_name,price\n101,Widget,9.99\n102,Gadget,12.49',
      'test3.csv': 'user_id,email\n3,test@example.com\n4,user@domain.com',
      'test4.csv': 'order_id,order_date,total\n1001,2024-09-01,59.99',
      'test5.csv': 'quote_id,quote\n1,"It\'s a beautiful day."\n2,"She said, ""Hello!"""'
  };

  beforeAll(() => {
      // Create the sample CSV files for testing
      for (const [filename, content] of Object.entries(testFiles)) {
          fs.writeFileSync(filename, content);
      }
  });

  afterAll(() => {
      // Remove the test files after tests
      for (const filename of Object.keys(testFiles)) {
          fs.unlinkSync(filename);
      }
  });

  it('should handle simple CSV correctly', () => {
      const expectedSql = (
          "INSERT INTO test1 (id, name, age) VALUES ('1', 'Alice', '30');\n" +
          "INSERT INTO test1 (id, name, age) VALUES ('2', 'Bob', '25');"
      );
      const result = csvToSqlInsert('test1.csv');
      expect(result).toEqual(expectedSql);
  });

  it('should handle product CSV correctly', () => {
      const expectedSql = (
          "INSERT INTO test2 (product_id, product_name, price) VALUES ('101', 'Widget', '9.99');\n" +
          "INSERT INTO test2 (product_id, product_name, price) VALUES ('102', 'Gadget', '12.49');"
      );
      const result = csvToSqlInsert('test2.csv');
      expect(result).toEqual(expectedSql);
  });

  it('should handle email CSV correctly', () => {
      const expectedSql = (
          "INSERT INTO test3 (user_id, email) VALUES ('3', 'test@example.com');\n" +
          "INSERT INTO test3 (user_id, email) VALUES ('4', 'user@domain.com');"
      );
      const result = csvToSqlInsert('test3.csv');
      expect(result).toEqual(expectedSql);
  });

  it('should handle date and decimal CSV correctly', () => {
      const expectedSql = (
          "INSERT INTO test4 (order_id, order_date, total) VALUES ('1001', '2024-09-01', '59.99');"
      );
      const result = csvToSqlInsert('test4.csv');
      expect(result).toEqual(expectedSql);
  });
});
