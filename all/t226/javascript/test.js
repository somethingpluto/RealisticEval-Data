const os = require('os');
const fs = require('fs');
const path = require('path');

describe('TestTSVtoJSONL', () => {
    let testDir;

    beforeAll(() => {
        // Create a temporary directory for testing
        testDir = fs.mkdtempSync(os.tmpdir() + 'jest-test-');
    });

    afterAll(() => {
        // Clean up the temporary directory
        fs.rmSync(testDir, { recursive: true, force: true });
    });

    const tsv_to_jsonl = require('./tsv_to_jsonl'); // Import the tsv_to_jsonl function

    test('standard TSV conversion', () => {
        const tsvContent = "Name\tAge\tCountry\nAlice\t30\tUSA\nBob\t25\tCanada\n";
        const tsvFile = path.join(testDir, 'test_standard.tsv');
        const jsonlFile = path.join(testDir, 'test_standard.jsonl');

        fs.writeFileSync(tsvFile, tsvContent, 'utf-8');

        tsv_to_jsonl(tsvFile, jsonlFile);

        const lines = fs.readFileSync(jsonlFile, 'utf-8').split('\n');

        const expectedLines = [
            '{"Name":"Alice","Age":30,"Country":"USA"}\n',
            '{"Name":"Bob","Age":25,"Country":"Canada"}\n'
        ];

        expect(lines).toEqual(expectedLines);
    });

    test('single row TSV conversion', () => {
        const tsvContent = "Name\tAge\tCountry\nAlice\t30\tUSA\n";
        const tsvFile = path.join(testDir, 'test_single_row.tsv');
        const jsonlFile = path.join(testDir, 'test_single_row.jsonl');

        fs.writeFileSync(tsvFile, tsvContent, 'utf-8');

        tsv_to_jsonl(tsvFile, jsonlFile);

        const lines = fs.readFileSync(jsonlFile, 'utf-8').split('\n');

        const expectedLines = [
            '{"Name":"Alice","Age":30,"Country":"USA"}\n'
        ];

        expect(lines).toEqual(expectedLines);
    });

    test('numeric and boolean values TSV conversion', () => {
        const tsvContent = "Name\tAge\tIs_Student\nAlice\t30\tTrue\nBob\t25\tFalse\n";
        const tsvFile = path.join(testDir, 'test_numeric_boolean.tsv');
        const jsonlFile = path.join(testDir, 'test_numeric_boolean.jsonl');

        fs.writeFileSync(tsvFile, tsvContent, 'utf-8');

        tsv_to_jsonl(tsvFile, jsonlFile);

        const lines = fs.readFileSync(jsonlFile, 'utf-8').split('\n');

        const expectedLines = [
            '{"Name":"Alice","Age":30,"Is_Student":true}\n',
            '{"Name":"Bob","Age":25,"Is_Student":false}\n'
        ];

        expect(lines).toEqual(expectedLines);
    });
});