describe('process_csv', () => {
  it('should remove rows with two or more empty columns', async () => {
    const inputFilePath = 'path/to/input.csv';
    const outputFilePath = 'path/to/output.csv';

    // Create a sample input CSV file
    const sampleInput = "col1,col2,col3\na,,b\nc,d,e\n";
    fs.writeFileSync(inputFilePath, sampleInput);

    await process_csv(inputFilePath, outputFilePath);

    // Read the output CSV file
    const outputContent = fs.readFileSync(outputFilePath, 'utf8');

    // Expected output without rows having two or more empty columns
    const expectedOutput = "col1,col2,col3\nc,d,e\n";

    expect(outputContent).toBe(expectedOutput);
  });

  it('should return an empty string if the file is empty', async () => {
    const inputFilePath = 'path/to/empty.csv';
    const outputFilePath = 'path/to/empty_output.csv';

    // Create an empty input CSV file
    const sampleInput = "";
    fs.writeFileSync(inputFilePath, sampleInput);

    await process_csv(inputFilePath, outputFilePath);

    // Check if the output file is empty
    const outputContent = fs.readFileSync(outputFilePath, 'utf8');
    expect(outputContent).toBe("");
  });
});