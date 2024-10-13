const fs = require('fs');
const diff = require('diff');
function compareFiles(file1Path: string, file2Path: string): string[] {
  /**
   * Compare the contents of two files and print the differences in unified diff format.
   *
   * @param file1Path - Path to the first file.
   * @param file2Path - Path to the second file.
   * @returns A list containing the lines of differences, if any.
   * @throws {Error} If either file does not exist or there is an error reading the files.
   */
  let lines1: string[];
  let lines2: string[];

  try {
      lines1 = fs.readFileSync(file1Path, 'utf8').split('\n');
      lines2 = fs.readFileSync(file2Path, 'utf8').split('\n');
  } catch (error) {
      if (error.code === 'ENOENT') {
          throw new Error('One of the files was not found.');
      }
      throw new Error(`Error reading files: ${error.message}`);
  }

  const diffLines = diff.unifiedDiff({
      fromFile: file1Path,
      toFile: file2Path,
      fromFileContent: lines1.join('\n'),
      toFileContent: lines2.join('\n')
  });

  if (diffLines) {
      diffLines.split('\n').forEach(line => console.log(line));
  }

  return diffLines ? diffLines.split('\n') : [];
}