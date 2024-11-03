import path from "path";


describe('TestAnswer', () => {
    const TEST_FILE = path.join(__dirname, 'testFile.txt');

    // Setup: Create a test file with initial content before each test
    beforeEach(() => {
        fs.writeFileSync(TEST_FILE, "Line 1\nLine 2\nLine 3\n");
    });

    // Teardown: Clean up the test file after each test
    afterEach(() => {
        try {
            fs.unlinkSync(TEST_FILE);
        } catch (err) {
            // If the file does not exist, we can safely ignore the error
        }
    });

    test('modify line success', () => {
        modifyLineInFile(TEST_FILE, 2, "Updated Line 2");
        const lines = fs.readFileSync(TEST_FILE, 'utf-8').split('\n');
        expect(lines[0]).toBe("Line 1");
        expect(lines[1]).toBe("Updated Line 2");
        expect(lines[2]).toBe("Line 3");
    });

    test('modify first line', () => {
        modifyLineInFile(TEST_FILE, 1, "Updated Line 1");
        const lines = fs.readFileSync(TEST_FILE, 'utf-8').split('\n');
        expect(lines[0]).toBe("Updated Line 1");
        expect(lines[1]).toBe("Line 2");
        expect(lines[2]).toBe("Line 3");
    });

    test('modify last line', () => {
        modifyLineInFile(TEST_FILE, 3, "Updated Line 3");
        const lines = fs.readFileSync(TEST_FILE, 'utf-8').split('\n');
        expect(lines[0]).toBe("Line 1");
        expect(lines[1]).toBe("Line 2");
        expect(lines[2]).toBe("Updated Line 3");
    });

    test('modify non-existent line', () => {
        expect(() => {
            modifyLineInFile(TEST_FILE, 4, "Should Fail");
        }).toThrow();
    });

    test('modify negative line number', () => {
        expect(() => {
            modifyLineInFile(TEST_FILE, 0, "Should Fail");
        }).toThrow();
    });
});