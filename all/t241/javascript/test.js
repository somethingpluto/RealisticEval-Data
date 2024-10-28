const fs = require('fs');
describe('TestGetMinDistance', () => {
    it('test basic functionality with expected input', () => {
        const mockContent = "hello world\napple banana apple\norange apple banana";
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([2, 1]);
    });

    it('test case where one or both words are not present', () => {
        const mockContent = "apple orange pear\norange pear apple";
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([null, Infinity]);
    });

    it('test an empty file', () => {
        const mockContent = '';
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([null, Infinity]);
    });

    it('test multiple lines with varying distances between words', () => {
        const mockContent = "apple banana\napple orange orange banana\napple orange orange orange banana";
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([1, 1]);
    });
});