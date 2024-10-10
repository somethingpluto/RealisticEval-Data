describe('findCommonColumns', () => {
    it('should return the common columns of all CSV files in a directory', () => {
        // Mocking the file system to simulate reading files
        const mockFiles = [
            'header1,header2,header3\nvalue1,value2,value3',
            'header1,header2,header4\nvalue4,value5,value6'
        ];

        const mockReadFileSync = jest.fn((filePath: string) => {
            const fileIndex = parseInt(filePath.split('/').pop()!.replace('.csv', ''), 10);
            return mockFiles[fileIndex];
        });

        jest.mock('fs', () => ({
            ...jest.requireActual('fs'),
            readFileSync: mockReadFileSync,
            readdirSync: jest.fn(() => ['file1.csv', 'file2.csv'])
        }));

        const result = findCommonColumns('./mockDirectory');

        expect(result).toEqual(['header1', 'header2']);
    });
});