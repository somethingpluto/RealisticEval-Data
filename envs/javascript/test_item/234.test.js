const fs = require('fs');
const csvParser = require('csv-parser');

/**
 * Appends a new row to a CSV file if there isn't a row with matching values in the first three columns.
 *
 * @param {fs.WriteStream} fileHandler - File handler of the CSV file opened in read-plus mode ('r+').
 * @param {csvParser} reader - CSV reader object for reading existing rows.
 * @param {Array} rowCandidate - Array containing the new row to be appended.
 */
function appendOrSkipRow(fileHandler, reader, rowCandidate) {
  let existingRows = [];
  let shouldAppend = true;

  // Read existing rows from the CSV file
  reader.on('data', (row) => {
    existingRows.push(row);
  });

  // Check if the new row already exists in the first three columns
  reader.on('end', () => {
    for (const existingRow of existingRows) {
      if (
        existingRow[reader.options.headers[0]] === rowCandidate[0] &&
        existingRow[reader.options.headers[1]] === rowCandidate[1] &&
        existingRow[reader.options.headers[2]] === rowCandidate[2]
      ) {
        shouldAppend = false;
        break;
      }
    }

    // Append the new row if it doesn't exist
    if (shouldAppend) {
      const newRowString = rowCandidate.join(',') + '\n';
      fileHandler.write(newRowString);
    }
  });
}

// Example usage:
// const fileStream = fs.createReadStream('path/to/your/csvfile.csv');
// const csvStream = csvParser({ headers: ['col1', 'col2', 'col3', 'col4'] });
// const fileHandler = fs.createWriteStream('path/to/your/csvfile.csv', { flags: 'r+' });

// appendOrSkipRow(fileHandler, csvStream, ['value1', 'value2', 'value3', 'value4']);
const { createWriteStream } = require('fs');
const { createStringReader } = require('csv-parser');
const { createObjectCsvWriter } = require('csv-writer');
describe('TestAppendOrSkipRow', () => {
  beforeEach(() => {
      // Set up a mock CSV file using a string buffer
      this.mockFile = new createStringReader('Alice,30,USA\nBob,25,UK\nCharlie,35,Canada\n');
      this.reader = this.mockFile;
  });

  afterEach(() => {
      // Reset the mock file for each test
      this.mockFile.reset();
  });

  it('test_append_new_row', () => {
      // Test appending a new row when there are no matching values
      const newRow = ['David', '28', 'Australia'];
      appendOrSkipRow(this.mockFile, this.reader, newRow);

      this.mockFile.reset();  // Reset pointer to read from the start
      const result = this.mockFile.readAll();
      expect(result).toContainEqual(newRow);
  });

  it('test_skip_different_values', () => {
      // Test appending a new row with different values
      const newRow = ['Alice', '31', 'USA'];  // Same name, different age
      appendOrSkipRow(this.mockFile, this.reader, newRow);

      this.mockFile.reset();  // Reset pointer to read from the start
      const result = this.mockFile.readAll();
      expect(result).toContainEqual(newRow);
  });

  it('test_append_row_with_different_columns', () => {
      // Test appending a row with different values in the first three columns
      const newRow = ['Eve', '40', 'Australia', 'Engineer'];
      appendOrSkipRow(this.mockFile, this.reader, newRow);

      this.mockFile.reset();  // Reset pointer to read from the start
      const result = this.mockFile.readAll();
      expect(result).toContainEqual(newRow);
  });

  it('test_multiple_appends', () => {
      // Test appending multiple new rows correctly
      const newRows = [
          ['Frank', '29', 'Germany'],
          ['Grace', '22', 'France']
      ];

      for (const row of newRows) {
          appendOrSkipRow(this.mockFile, this.reader, row);
          this.mockFile.reset();  // Reset pointer for the next read
          this.reader = this.mockFile;
      }

      this.mockFile.reset();  // Reset pointer to read from the start
      const result = this.mockFile.readAll();
      newRows.forEach(row => expect(result).toContainEqual(row));
  });
});
