import * as os from 'os';
import * as fs from 'fs';
import * as path from 'path';
import * as fsExtra from 'fs-extra';
import * as tmp from 'tmp';

describe('TestEmptyDirectory', () => {
  let testDir: string;

  beforeAll(() => {
      // Set up a temporary directory with some files and directories
      testDir = tmp.dirSync().name;
      fs.mkdirSync(path.join(testDir, 'subdir'));
      fs.writeFileSync(path.join(testDir, 'file1.txt'), "Hello");
      fs.writeFileSync(path.join(testDir, 'subdir', 'file2.txt'), "World");
  });

  afterAll(() => {
      // Remove the temporary directory after all tests
      fsExtra.removeSync(testDir);
  });

  it('should empty the directory successfully', () => {
      emptyDirectory(testDir);
      expect(fs.readdirSync(testDir)).toEqual([]);
  });

  it('should empty a directory that includes subdirectories', () => {
      emptyDirectory(testDir);
      expect(fs.readdirSync(testDir)).toEqual([]);
  });

  it('should handle an already empty directory', () => {
      emptyDirectory(testDir);  // First emptying
      emptyDirectory(testDir);  // Empty again
      expect(fs.readdirSync(testDir)).toEqual([]);
  });
});