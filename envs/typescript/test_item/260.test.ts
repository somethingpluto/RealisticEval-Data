// Add the following lines at the start of your existing function
import { promisify } from 'util';
import { readFile, writeFile } from 'fs/promises';
import { createReadStream } from 'fs';
import { join } from 'path';

// Replace the existing fs.readFile and fs.writeFile with the following
const readFileAsync = promisify(readFile);
const writeFileAsync = promisify(writeFile);

// Modify the processCsv function to use async/await
async function processCsv(file_path: string, output_path: string): Promise<void> {
  try {
    const data = await readFileAsync(join(__dirname, file_path), 'utf8');
    const records = csvParser.parse(data);
    const filteredRecords = records.filter(record => {
      const emptyColumns = record.filter(field => field === '');
      return emptyColumns.length < 2;
    });

    const csvWriterInstance = csvWriter.createObjectCsvWriter({
      path: output_path,
      header: filteredRecords[0] ? Object.keys(filteredRecords[0]) : []
    });

    await csvWriterInstance.writeRecords(filteredRecords);
  } catch (error) {
    console.error('Error processing CSV file:', error);
  }
}
import { readFileSync, writeFileSync, unlinkSync } from 'fs';
import { join } from 'path';

describe('TestProcessCSV', () => {
  let input_data_1: string;
  let input_data_2: string;
  let input_data_3: string;

  beforeEach(() => {
    input_data_1 = `A,B,C
1,2,3
4,,6
7,8,
9,10,11`;

    input_data_2 = `A,B,C,D
,,
1,,3,4
2,3,,5
,,,`;

    input_data_3 = `A
1
2
3`;
  });

  const process_data = (input_data: string): string => {
    const inputFilePath = 'input.csv';
    const outputFilePath = 'output.csv';

    // Write input data to a temp CSV file
    writeFileSync(inputFilePath, input_data);

    // Process the CSV
    processCsv(inputFilePath, outputFilePath);

    // Read the output
    const outputData = readFileSync(outputFilePath, 'utf8');

    // Clean up temp files
    unlinkSync(inputFilePath);
    unlinkSync(outputFilePath);

    return outputData;
  };

  it('should correctly process input_data_1', () => {
    const output = process_data(input_data_1);
    const expectedOutput = `A,B,C\n1,2.0,3.0\n4,,6.0\n7,8.0,\n9,10.0,11.0\n`;
    expect(output).toEqual(expectedOutput);
  });

  it('should correctly process input_data_2', () => {
    const output = process_data(input_data_2);
    const expectedOutput = `A,B,C,D\n1.0,,3.0,4.0\n2.0,3.0,,5.0\n`;
    expect(output).toEqual(expectedOutput);
  });

  it('should correctly process input_data_3', () => {
    const output = process_data(input_data_3);
    const expectedOutput = `A\n1\n2\n3\n`; // Single-column CSV should remain unchanged
    expect(output).toEqual(expectedOutput);
  });
});
