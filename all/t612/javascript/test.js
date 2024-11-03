import path from "path";

describe('TestFindAndReplace', () => {
    let tempDir;

    beforeAll(() => {
        // Create a temporary directory for the tests
        tempDir = path.join(__dirname, 'temp');
        fs.mkdirSync(tempDir, { recursive: true });
    });

    afterAll(() => {
        // Remove the temporary directory after tests
        fs.readdirSync(tempDir).forEach(file => {
            fs.unlinkSync(path.join(tempDir, file));
        });
        fs.rmdirSync(tempDir);
    });

    // Test case 1: Basic find and replace
    test('find and replace basic', () => {
        const filePath = path.join(tempDir, 'testfile.txt');
        fs.writeFileSync(filePath, 'Hello World\nGoodbye World\n');

        findAndReplaceInFile(filePath, 'World', 'Java');

        const result = fs.readFileSync(filePath, 'utf-8').split('\n');
        expect(result).toEqual(['Hello Java', 'Goodbye Java', '']);
    });

    // Test case 2: No occurrences of the search string
    test('find and replace no occurrences', () => {
        const filePath = path.join(tempDir, 'testfile.txt');
        fs.writeFileSync(filePath, 'Hello World\nGoodbye World\n');

        findAndReplaceInFile(filePath, 'Python', 'Java');

        const result = fs.readFileSync(filePath, 'utf-8').split('\n');
        expect(result).toEqual(['Hello World', 'Goodbye World', '']);
    });

    // Test case 3: Multiple occurrences in a single line
    test('find and replace multiple occurrences', () => {
        const filePath = path.join(tempDir, 'testfile.txt');
        fs.writeFileSync(filePath, 'Hello World World\nGoodbye World\n');

        findAndReplaceInFile(filePath, 'World', 'Java');

        const result = fs.readFileSync(filePath, 'utf-8').split('\n');
        expect(result).toEqual(['Hello Java Java', 'Goodbye Java', '']);
    });

    // Test case 4: Replace with an empty string
    test('find and replace with empty string', () => {
        const filePath = path.join(tempDir, 'testfile.txt');
        fs.writeFileSync(filePath, 'Hello World\nGoodbye World\n');

        findAndReplaceInFile(filePath, 'World', '');

        const result = fs.readFileSync(filePath, 'utf-8').split('\n');
        expect(result).toEqual(['Hello ', 'Goodbye ', '']);
    });

    // Test case 5: Empty file
    test('find and replace empty file', () => {
        const filePath = path.join(tempDir, 'testfile.txt');
        fs.writeFileSync(filePath, '\n');

        findAndReplaceInFile(filePath, 'World', 'Java');

        const result = fs.readFileSync(filePath, 'utf-8').split('\n');
        expect(result).toEqual(['', '']);
    });
});