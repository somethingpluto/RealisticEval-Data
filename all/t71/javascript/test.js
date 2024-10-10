describe('readColumns', () => {
    it('should read numerical columns correctly', () => {
        // Mock the file content
        const mockFilePath = path.join(__dirname, 'mock.txt');
        const mockContent = `line1\nline2/with/some/data\n4 5 6\n7 8 9`;
        fs.writeFileSync(mockFilePath, mockContent);

        const result = readColumns(mockFilePath);
        expect(result).toEqual([[4, 5, 6], [7, 8, 9]]);

        // Clean up the mock file
        fs.unlinkSync(mockFilePath);
    });

    it('should throw an error if no \'/\' character is found', () => {
        // Mock the file content without a '/'
        const mockFilePath = path.join(__dirname, 'mock_no_slash.txt');
        const mockContent = `line1\nline2\n3 4 5`;
        fs.writeFileSync(mockFilePath, mockContent);

        expect(() => readColumns(mockFilePath)).toThrow('File does not contain any \'/\' character.');

        // Clean up the mock file
        fs.unlinkSync(mockFilePath);
    });
});
