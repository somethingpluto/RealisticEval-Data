const fs = require('fs');
const path = require('path');
describe('Classify JSON Objects by PID', () => {
  let tempDir;
  let sourceFile;
  let matchFile;
  let mismatchFile;
  
  beforeAll(() => {
    // Create a temporary directory
    tempDir = fs.mkdtempSync(path.join(__dirname, 'temp-'));
    
    // Create temporary files for testing
    sourceFile = path.join(tempDir, 'source.json');
    matchFile = path.join(tempDir, 'match.json');
    mismatchFile = path.join(tempDir, 'mismatch.json');
    
    // Example data
    const data = [
      { name: "Alice", pid: 1 },
      { name: "Bob", pid: 2 },
      { name: "Charlie", pid: 3 }
    ];

    // Write example data to source file
    fs.writeFileSync(sourceFile, JSON.stringify(data));
  });

  afterAll(() => {
    // Clean up temporary files and directory
    fs.rmSync(tempDir, { recursive: true, force: true });
  });

  test('all match', () => {
    classifyJsonObjectsByPid(sourceFile, [1, 2, 3], matchFile, mismatchFile);
    
    const matches = JSON.parse(fs.readFileSync(matchFile, 'utf8'));
    const mismatches = JSON.parse(fs.readFileSync(mismatchFile, 'utf8'));

    expect(matches.length).toBe(3);
    expect(mismatches.length).toBe(0);
  });

  test('no match', () => {
    classifyJsonObjectsByPid(sourceFile, [4, 5], matchFile, mismatchFile);
    
    const matches = JSON.parse(fs.readFileSync(matchFile, 'utf8'));
    const mismatches = JSON.parse(fs.readFileSync(mismatchFile, 'utf8'));

    expect(matches.length).toBe(0);
    expect(mismatches.length).toBe(3);
  });

  test('partial match', () => {
    classifyJsonObjectsByPid(sourceFile, [1, 3], matchFile, mismatchFile);
    
    const matches = JSON.parse(fs.readFileSync(matchFile, 'utf8'));
    const mismatches = JSON.parse(fs.readFileSync(mismatchFile, 'utf8'));

    expect(matches.length).toBe(2);
    expect(mismatches.length).toBe(1);
  });

  test('empty PID list', () => {
    classifyJsonObjectsByPid(sourceFile, [], matchFile, mismatchFile);
    
    const matches = JSON.parse(fs.readFileSync(matchFile, 'utf8'));
    const mismatches = JSON.parse(fs.readFileSync(mismatchFile, 'utf8'));

    expect(matches.length).toBe(0);
    expect(mismatches.length).toBe(3);
  });
});
