const fs = require('fs');
const path = require('path');
const { findJsonFilesWithKeyword } = require('./your-module'); // Adjust the import as necessary

const mockFs = require('mock-fs');

describe('findJsonFilesWithKeyword', () => {
    beforeAll(() => {
        jest.spyOn(fs, 'readdirSync');
        jest.spyOn(fs, 'statSync');
        jest.spyOn(fs, 'readFileSync');
    });

    afterAll(() => {
        jest.restoreAllMocks();
        mockFs.restore();
    });

    afterEach(() => {
        mockFs.restore();
    });

    test('keyword in single file', () => {
        mockFs({
            'test_dir': {
                'test.js.json': '{"key": "value with keyword"}'
            }
        });

        const result = findJsonFilesWithKeyword('test_dir', 'keyword');
        expect(result).toEqual(['test.js.json']);
    });

    test('keyword not in file', () => {
        mockFs({
            'test_dir': {
                'test.js.json': '{"key": "no keyword here"}'
            }
        });

        const result = findJsonFilesWithKeyword('test_dir', 'wc');
        expect(result).toEqual([]);
    });

    test('no JSON files in directory', () => {
        mockFs({
            'test_dir': {}
        });

        const result = findJsonFilesWithKeyword('test_dir', 'keyword');
        expect(result).toEqual([]);
    });

    test('multiple JSON files', () => {
        mockFs({
            'test_dir': {
                'file1.json': '{"key": "keyword present here"}',
                'file2.json': '{"key": "keyword present here"}'
            }
        });

        const result = findJsonFilesWithKeyword('test_dir', 'keyword');
        expect(result).toEqual(['file1.json', 'file2.json']);
    });
});