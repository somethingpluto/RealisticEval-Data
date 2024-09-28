const fs = require('fs');
const path = require('path');
const os = require('os');
const { classifyJsonObjectsByPid } = require('./yourModule'); // Assuming your function is exported from this module

describe('Test classifyJsonObjectsByPid', () => {
    let tempDir;
    let sourceFile;
    let matchFile;
    let mismatchFile;
    const data = [
        { name: 'Alice', pid: 1 },
        { name: 'Bob', pid: 2 },
        { name: 'Charlie', pid: 3 }
    ];
    const pidList = [1, 3];

    beforeAll(() => {
        // Create a temporary directory
        tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'test-'));

        // Define file paths
        sourceFile = path.join(tempDir, 'source.json');
        matchFile = path.join(tempDir, 'match.json');
        mismatchFile = path.join(tempDir, 'mismatch.json');

        // Write example data to source file
        fs.writeFileSync(sourceFile, JSON.stringify(data), 'utf8');
    });

    afterAll(() => {
        // Clean up temporary files
        fs.unlinkSync(sourceFile);
        fs.unlinkSync(matchFile);
        fs.unlinkSync(mismatchFile);
        fs.rmdirSync(tempDir);
    });

    test('all items match', () => {
        classifyJsonObjectsByPid(sourceFile, [1, 2, 3], matchFile, mismatchFile);
        
        const matches = JSON.parse(fs.readFileSync(matchFile, 'utf8'));
        const mismatches = JSON.parse(fs.readFileSync(mismatchFile, 'utf8'));
        
        expect(matches).toHaveLength(3);
        expect(mismatches).toHaveLength(0);
    });

    test('no items match', () => {
        classifyJsonObjectsByPid(sourceFile, [4, 5], matchFile, mismatchFile);
        
        const matches = JSON.parse(fs.readFileSync(matchFile, 'utf8'));
        const mismatches = JSON.parse(fs.readFileSync(mismatchFile, 'utf8'));
        
        expect(matches).toHaveLength(0);
        expect(mismatches).toHaveLength(3);
    });

    test('partial items match', () => {
        classifyJsonObjectsByPid(sourceFile, pidList, matchFile, mismatchFile);
        
        const matches = JSON.parse(fs.readFileSync(matchFile, 'utf8'));
        const mismatches = JSON.parse(fs.readFileSync(mismatchFile, 'utf8'));
        
        expect(matches).toHaveLength(2);
        expect(mismatches).toHaveLength(1);
    });

    test('empty PID list', () => {
        classifyJsonObjectsByPid(sourceFile, [], matchFile, mismatchFile);
        
        const matches = JSON.parse(fs.readFileSync(matchFile, 'utf8'));
        const mismatches = JSON.parse(fs.readFileSync(mismatchFile, 'utf8'));
        
        expect(matches).toHaveLength(0);
        expect(mismatches).toHaveLength(3);
    });
});