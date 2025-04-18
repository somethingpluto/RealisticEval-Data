import fs from 'fs';
import path from 'path';

describe('TestProcessCSV', () => {
    let input_data_1 = `A,B,C
1,2,3
4,,6
7,8,
9,10,11`;

    let input_data_2 = `A,B,C,D
,,
1,,3,4
2,3,,5
,,,`;

    let input_data_3 = `A
1
2
3`;

    beforeEach(() => {
        // Temporary directory for test files
        const tempDir = os.tmpdir();
        const inputFilePath = path.join(tempDir, 'input.csv');
        const outputFilePath = path.join(tempDir, 'output.csv');

        // Helper function to process data
        const process_data = (input_data) => {
            // Write input data to a qa_item CSV file
            fs.writeFileSync(inputFilePath, input_data);

            // Process the CSV
            processCSV(inputFilePath, outputFilePath);

            // Read the output
            const output_data = fs.readFileSync(outputFilePath, 'utf8');

            // Clean up qa_item files
            fs.unlinkSync(inputFilePath);
            fs.unlinkSync(outputFilePath);

            return output_data;
        };

        // Test cases
        test('test_case_1', async () => {
            const output = process_data(input_data_1);
            const expected_output = `A,B,C\n1,2.0,3.0\n4,,6.0\n7,8.0,\n9,10.0,11.0\n`;
            expect(output).toEqual(expected_output);
        });

        test('test_case_2', async () => {
            const output = process_data(input_data_2);
            const expected_output = `A,B,C,D\n1.0,,3.0,4.0\n2.0,3.0,,5.0\n`;
            expect(output).toEqual(expected_output);
        });

        test('test_case_3', async () => {
            const output = process_data(input_data_3);
            const expected_output = `A\n1\n2\n3\n`; // Single-column CSV should remain unchanged
            expect(output).toEqual(expected_output);
        });
    });
});