const fs = require('fs');

/**
 * Classifies JSON objects by pid and writes matches and mismatches to separate files.
 * 
 * @param {string} sourceFile - Path to the source JSON file.
 * @param {Array} pidList - List of pids to match.
 * @param {string} matchFile - Path to save matching objects JSON.
 * @param {string} mismatchFile - Path to save mismatching objects JSON.
 */
function classifyJsonObjectsByPid(sourceFile, pidList, matchFile, mismatchFile) {
    // Read the source JSON file
    fs.readFile(sourceFile, 'utf8', (err, data) => {
        if (err) {
            console.error(`Error reading source file: ${err}`);
            return;
        }

        try {
            // Parse the JSON data
            const jsonData = JSON.parse(data);

            // Initialize arrays to hold matching and mismatching objects
            const matches = [];
            const mismatches = [];

            // Iterate through each object in the JSON data
            jsonData.forEach(obj => {
                // Check if the object's pid is in the pidList
                if (pidList.includes(obj.pid)) {
                    matches.push(obj);
                } else {
                    mismatches.push(obj);
                }
            });

            // Write matching objects to the match file
            fs.writeFile(matchFile, JSON.stringify(matches, null, 2), 'utf8', err => {
                if (err) {
                    console.error(`Error writing to match file: ${err}`);
                }
            });

            // Write mismatching objects to the mismatch file
            fs.writeFile(mismatchFile, JSON.stringify(mismatches, null, 2), 'utf8', err => {
                if (err) {
                    console.error(`Error writing to mismatch file: ${err}`);
                }
            });

        } catch (parseErr) {
            console.error(`Error parsing JSON: ${parseErr}`);
        }
    });
}
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

