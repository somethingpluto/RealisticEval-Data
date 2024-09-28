const { renameFilePath } = require('./pathToYourFunction'); // Adjust the import based on your file structure

describe('renameFilePath', () => {
    test('renames path with colon in filename', () => {
        const path = 'C:\\Users\\example\\Documents\\report:2023.txt';
        const expected = 'C:\\Users\\example\\Documents\\report_2023.txt';
        expect(renameFilePath(path)).toBe(expected);
    });

    test('renames path without colon in filename', () => {
        const path = 'C:\\Users\\example\\Documents\\report2023.txt';
        const expected = 'C:\\Users\\example\\Documents\\report2023.txt';
        expect(renameFilePath(path)).toBe(expected);
    });

    test('renames path with multiple colons in filename', () => {
        const path = 'C:\\Users\\example\\Documents\\project:report:2023.txt';
        const expected = 'C:\\Users\\example\\Documents\\project_report_2023.txt';
        expect(renameFilePath(path)).toBe(expected);
    });

    test('renames path with colon at end of filename', () => {
        const path = 'C:\\Users\\example\\Documents\\backup:';
        const expected = 'C:\\Users\\example\\Documents\\backup_';
        expect(renameFilePath(path)).toBe(expected);
    });

    test('renames path with colon at start of filename', () => {
        const path = 'C:\\Users\\example\\Documents\\:initial_setup.txt';
        const expected = 'C:\\Users\\example\\Documents\\_initial_setup.txt';
        expect(renameFilePath(path)).toBe(expected);
    });
});