describe('TestSaveContentToFile', () => {
    let testFilePath = 'test_output.txt';

    beforeAll(() => {
        // Set up a temporary file path for testing
        testFilePath = 'test_output.txt';
    });

    afterAll(() => {
        // Clean up the test file after all tests
        if (fs.existsSync(testFilePath)) {
            fs.unlinkSync(testFilePath);
        }
    });

    beforeEach(() => {
        // Ensure the test file is clean before each test
        if (fs.existsSync(testFilePath)) {
            fs.unlinkSync(testFilePath);
        }
    });

    afterEach(() => {
        // Clean up the test file after each test
        if (fs.existsSync(testFilePath)) {
            fs.unlinkSync(testFilePath);
        }
    });

    it('should save basic content correctly', () => {
        const content = "Hello,  World!  ";
        const expected = "Hello, World!";
        saveContentToFile(content, testFilePath);
        const result = fs.readFileSync(testFilePath, 'utf-8').trim();
        expect(result).toEqual(expected);
    });

    it('should handle multiple spaces and empty lines correctly', () => {
        const content = `

        This is a    test.

        Another line.      
        `;
        const expected = "This is a test. Another line.";
        saveContentToFile(content, testFilePath);
        const result = fs.readFileSync(testFilePath, 'utf-8').trim();
        expect(result).toEqual(expected);
    });

    it('should handle only whitespace correctly', () => {
        const content = "    \n  \n   ";
        const expected = "";
        saveContentToFile(content, testFilePath);
        const result = fs.readFileSync(testFilePath, 'utf-8').trim();
        expect(result).toEqual(expected);
    });

    it('should handle empty content correctly', () => {
        const content = "";
        const expected = "";
        saveContentToFile(content, testFilePath);
        const result = fs.readFileSync(testFilePath, 'utf-8').trim();
        expect(result).toEqual(expected);
    });
});