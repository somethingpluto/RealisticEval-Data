describe('dataframe_to_markdown function', () => {
    const testData = [
        {
            input: {
                df: new Map([
                    ['Name', ['Alice', 'Bob']],
                    ['Age', [25, 30]]
                ]),
                md_path: '/tmp/test_output.md'
            },
            expected: '| Name | Age |\n| --- | --- |\n| Alice | 25 |\n| Bob | 30 |\n'
        }
    ];

    testData.forEach(({ input, expected }, index) => {
        test(`should convert dataframe to markdown correctly for test case ${index + 1}`, async () => {
            // Mocking the fs.writeFile method
            const mockWriteFile = jest.spyOn(fs, 'writeFileSync');
            mockWriteFile.mockImplementation(() => {});

            // Call the function with the test data
            await dataframe_to_markdown(input.df, input.md_path);

            // Check if the function was called with the correct arguments
            expect(mockWriteFile).toHaveBeenCalledWith(
                input.md_path,
                expected
            );

            // Clean up the mock
            mockWriteFile.mockRestore();
        });
    });
});