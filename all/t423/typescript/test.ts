describe('TestWriteUniqueLineToFile', () => {
    let filename: string;

    beforeAll(() => {
        // Setup: create a temporary file for testing.
        filename = 'test_file.txt';
        fs.writeFileSync(filename, '');
    });

    afterAll(() => {
        // Cleanup: remove the temporary file after all tests.
        fs.unlinkSync(filename);
    });

    it('writes a new line to an empty file', () => {
        const lineContent = "First unique line.";
        writeUniqueLineToFile(filename, lineContent);

        const fileContent = fs.readFileSync(filename, 'utf8');
        expect(fileContent).toContain(lineContent);
    });

    it('does not write a duplicate line', () => {
        const lineContent = "First unique line.";
        writeUniqueLineToFile(filename, lineContent);
        writeUniqueLineToFile(filename, lineContent);

        const fileContent = fs.readFileSync(filename, 'utf8');
        expect(fileContent.split('\n').filter(line => line === lineContent).length).toBe(1);
    });

    it('writes multiple unique lines', () => {
        const lines = ["First unique line.", "Second unique line.", "Third unique line."];
        lines.forEach(line => writeUniqueLineToFile(filename, line));

        const fileContent = fs.readFileSync(filename, 'utf8');
        lines.forEach(line => {
            expect(fileContent).toContain(line);
        });
    });

    it('does not write an empty line', () => {
        const lineContent = "";
        writeUniqueLineToFile(filename, lineContent);

        const fileContent = fs.readFileSync(filename, 'utf8');
        expect(fileContent.trim()).toBe("");
    });
});