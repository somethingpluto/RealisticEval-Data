const fs = require('fs');

describe('TestGetMinDistance', () => {
    beforeEach(() => {
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => '');
    });

    afterEach(() => {
        fs.readFileSync.mockRestore();
    });

    test('test simple case', () => {
        // Mock the file read operation
        fs.readFileSync.mockImplementation(() => {
            return Buffer.from(`
                hello world
                hello hello world
                world hello
            `);
        });

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 1]);
    });

    test('test multiple lines', () => {
        fs.readFileSync.mockImplementation(() => {
            return Buffer.from(`
                hello planet
                world hello planet
                hello world planet
            `);
        });

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([1, 1]);
    });

    test('test large distance', () => {
        fs.readFileSync.mockImplementation(() => {
            return Buffer.from(`
                hello a b c d e f g h i j k l m n o p q r s t u v w x y z world
            `);
        });

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 27]);
    });

    test('test adjacent words', () => {
        fs.readFileSync.mockImplementation(() => {
            return Buffer.from(`
                hello world
                hello hello world world
                world hello
            `);
        });

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 1]);
    });
});