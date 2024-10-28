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