describe('processCsv', () => {
    it('should remove rows with two or more empty columns', () => {
        const inputFilePath = 'path/to/input.csv';
        const outputFilePath = 'path/to/output.csv';

        // Sample input data
        const inputData = `
id,name,email,age
1,Alice,,25
2,Bob,bob@example.com,
3,,charlie@example.com,30
4,David,david@example.com,35
`;

        // Write sample input data to a temporary file
        writeFileSync(inputFilePath, inputData);

        // Call the function under test
        processCsv(inputFilePath, outputFilePath);

        // Read the output file
        const outputFileData = readFileSync(outputFilePath, 'utf8');

        // Expected output data after processing
        const expectedOutputData = `
id,name,email,age
2,Bob,bob@example.com,
4,David,david@example.com,35
`;

        // Check if the output matches the expected data
        expect(outputFileData.trim()).toBe(expectedOutputData.trim());
    });

    it('should handle an empty input file gracefully', () => {
        const inputFilePath = 'path/to/empty_input.csv';
        const outputFilePath = 'path/to/empty_output.csv';

        // Create an empty input file
        writeFileSync(inputFilePath, '');

        // Call the function under test
        processCsv(inputFilePath, outputFilePath);

        // Check if the output file is empty
        const outputFileData = readFileSync(outputFilePath, 'utf8');
        expect(outputFileData).toBe('');
    });
});