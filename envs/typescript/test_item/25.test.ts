// ... (previous code for context)

import { readFile, writeFile } from 'fs/promises';
import { join } from 'path';
import { promisify } from 'util';
import { exec } from 'child_process';

const readFileAsync = promisify(readFile);
const writeFileAsync = promisify(writeFile);

async function classifyJsonObjectsByPid(
    sourceFile: string,
    pidList: string[],
    matchFile: string,
    mismatchFile: string
): Promise<void> {
    try {
        const fileContent = await readFileAsync(sourceFile, 'utf8');
        const jsonObjects: JsonObject[] = JSON.parse(fileContent);

        const matches: JsonObject[] = [];
        const mismatches: JsonObject[] = [];

        jsonObjects.forEach((jsonObj) => {
            const pid = jsonObj.pid;
            if (pidList.includes(pid)) {
                matches.push(jsonObj);
            } else {
                mismatches.push(jsonObj);
            }
        });

        await writeFileAsync(matchFile, JSON.stringify(matches, null, 2));
        await writeFileAsync(mismatchFile, JSON.stringify(mismatches, null, 2));

        // Call Python script for post-processing
        const pythonScriptPath = join(__dirname, 'post_process.py');
        await exec(`python "${pythonScriptPath}" "${matchFile}" "${mismatchFile}"`);
    } catch (error) {
        console.error('Error classifying JSON objects:', error);
    }
}

// ... (rest of the code)
import fs from 'fs';
import path from 'path';

interface DataObject {
  name: string;
  pid: number;
}

describe('classifyJsonObjectsByPid', () => {
  const tempDir = fs.mkdtempSync(path.join(__dirname, 'temp-'));
  const sourceFile = path.join(tempDir, 'source.json');
  const matchFile = path.join(tempDir, 'match.json');
  const mismatchFile = path.join(tempDir, 'mismatch.json');

  const data: DataObject[] = [
    { name: 'Alice', pid: 1 },
    { name: 'Bob', pid: 2 },
    { name: 'Charlie', pid: 3 }
  ];
  
  const pidList = [1, 3];

  beforeAll(() => {
    // Write example data to source file
    fs.writeFileSync(sourceFile, JSON.stringify(data));
  });

  afterAll(() => {
    // Cleanup temporary directory
    fs.rmdirSync(tempDir, { recursive: true });
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
    classifyJsonObjectsByPid(sourceFile, pidList, matchFile, mismatchFile);
    
    const matches = JSON.parse(fs.readFileSync(matchFile, 'utf8'));
    const mismatches = JSON.parse(fs.readFileSync(mismatchFile, 'utf8'));

    expect(matches.length).toBe(2);
    expect(mismatches.length).toBe(1);
  });

  test('empty pid list', () => {
    classifyJsonObjectsByPid(sourceFile, [], matchFile, mismatchFile);
    
    const matches = JSON.parse(fs.readFileSync(matchFile, 'utf8'));
    const mismatches = JSON.parse(fs.readFileSync(mismatchFile, 'utf8'));

    expect(matches.length).toBe(0);
    expect(mismatches.length).toBe(3);
  });
});

