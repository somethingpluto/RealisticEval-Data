import { readFile, writeFile } from 'fs';


describe('TestExtractFiles', () => {
    const folderA = path.join(__dirname, 'test_folderA');
    const folderB = path.join(__dirname, 'test_folderB');

    beforeEach(() => {
        // Set up test directories
        fs.mkdirSync(folderA, { recursive: true });
        fs.mkdirSync(folderB, { recursive: true });
    });

    afterEach(() => {
        // Clean up test directories
        fs.rmdirSync(folderA, { recursive: true });
        fs.rmdirSync(folderB, { recursive: true });
    });

    const createCSV = (filenameList) => {
        // Helper function to create a CSV file for testing
        const csvFile = path.join(__dirname, 'test_exclude.csv');
        const csvContent = 'filename\n' + filenameList.join('\n');
        fs.writeFileSync(csvFile, csvContent);
        return csvFile;
    };

    test('basic functionality with some files excluded', () => {
        // Create test files in folderA
        fs.writeFileSync(path.join(folderA, 'file1.txt'), 'Content of file 1');
        fs.writeFileSync(path.join(folderA, 'file2.txt'), 'Content of file 2');
        fs.writeFileSync(path.join(folderA, 'file3.txt'), 'Content of file 3');

        const csvFile = createCSV(['file2.txt']); // Exclude file2.txt
        extractFilesExcludingCSV(folderA, csvFile, folderB);

        expect(fs.existsSync(path.join(folderB, 'file1.txt'))).toBe(true);
        expect(fs.existsSync(path.join(folderB, 'file2.txt'))).toBe(false);
        expect(fs.existsSync(path.join(folderB, 'file3.txt'))).toBe(true);
    });

    test('when folderA is empty', () => {
        const csvFile = createCSV(['file1.txt']); // Exclude file1.txt
        extractFilesExcludingCSV(folderA, csvFile, folderB);

        expect(fs.readdirSync(folderB).length).toBe(0);
    });

    test('when all files are excluded', () => {
        // Create test files in folderA
        fs.writeFileSync(path.join(folderA, 'file1.txt'), 'Content of file 1');
        fs.writeFileSync(path.join(folderA, 'file2.txt'), 'Content of file 2');

        const csvFile = createCSV(['file1.txt', 'file2.txt']); // Exclude all files
        extractFilesExcludingCSV(folderA, csvFile, folderB);

        expect(fs.readdirSync(folderB).length).toBe(0);
    });

    test('when folderB already contains files', () => {
        fs.writeFileSync(path.join(folderB, 'existing_file.txt'), 'This is an existing file.');

        fs.writeFileSync(path.join(folderA, 'file1.txt'), 'Content of file 1');

        const csvFile = createCSV([]); // Do not exclude any files
        extractFilesExcludingCSV(folderA, csvFile, folderB);

        expect(fs.existsSync(path.join(folderB, 'existing_file.txt'))).toBe(true);
        expect(fs.existsSync(path.join(folderB, 'file1.txt'))).toBe(true);
    });

    test('with an empty CSV file', () => {
        fs.writeFileSync(path.join(folderA, 'file1.txt'), 'Content of file 1');

        const csvFile = createCSV([]); // Empty CSV, do not exclude any files
        extractFilesExcludingCSV(folderA, csvFile, folderB);

        expect(fs.existsSync(path.join(folderB, 'file1.txt'))).toBe(true);
    });
});
