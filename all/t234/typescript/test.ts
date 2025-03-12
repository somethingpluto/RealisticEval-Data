import * as fs from 'fs';
import * as csvParser from 'csv-parser';
import * as createCsvWriter from 'csv-writer';
describe('TestAppendOrSkipRow', () => {
  let mockFile: fs.WriteStream;
  let reader: csvParser.CSVParser;

  beforeEach(() => {
    // Set up a mock CSV file using a temporary file
    const tempFilePath = 'qa_item.csv';
    mockFile = fs.createWriteStream(tempFilePath);
    mockFile.write('Alice,30,USA\nBob,25,UK\nCharlie,35,Canada\n');
    mockFile.end();

    // Wait for the file to be written
    return new Promise(resolve => mockFile.on('finish', resolve)).then(() => {
      mockFile = fs.createReadStream(tempFilePath);
      reader = csvParser();
    });
  });

  afterEach(() => {
    // Clean up the temporary file
    fs.unlinkSync('qa_item.csv');
  });

  it('should append a new row when there are no matching values', () => {
    const new_row = ['David', '28', 'Australia'];
    appendOrSkipRow(mockFile, reader, new_row);

    // Reset pointer to read from the start
    mockFile = fs.createReadStream('qa_item.csv');
    reader = csvParser();

    const results: string[][] = [];
    mockFile
      .pipe(reader)
      .on('data', (row) => {
        results.push(Object.values(row));
      })
      .on('end', () => {
        expect(results).toContainEqual(new_row);
      });
  });

  it('should append a new row with different values', () => {
    const new_row = ['Alice', '31', 'USA']; // Same name, different age
    appendOrSkipRow(mockFile, reader, new_row);

    // Reset pointer to read from the start
    mockFile = fs.createReadStream('qa_item.csv');
    reader = csvParser();

    const results: string[][] = [];
    mockFile
      .pipe(reader)
      .on('data', (row) => {
        results.push(Object.values(row));
      })
      .on('end', () => {
        expect(results).toContainEqual(new_row);
      });
  });

  it('should append a row with different values in the first three columns', () => {
    const new_row = ['Eve', '40', 'Australia', 'Engineer'];
    appendOrSkipRow(mockFile, reader, new_row);

    // Reset pointer to read from the start
    mockFile = fs.createReadStream('qa_item.csv');
    reader = csvParser();

    const results: string[][] = [];
    mockFile
      .pipe(reader)
      .on('data', (row) => {
        results.push(Object.values(row));
      })
      .on('end', () => {
        expect(results).toContainEqual(new_row);
      });
  });

  it('should append multiple new rows correctly', () => {
    const new_rows = [
      ['Frank', '29', 'Germany'],
      ['Grace', '22', 'France']
    ];

    for (const row of new_rows) {
      appendOrSkipRow(mockFile, reader, row);
      mockFile = fs.createReadStream('qa_item.csv');
      reader = csvParser();
    }

    const results: string[][] = [];
    mockFile
      .pipe(reader)
      .on('data', (row) => {
        results.push(Object.values(row));
      })
      .on('end', () => {
        new_rows.forEach(row => expect(results).toContainEqual(row));
      });
  });
});