import { emptyDirectory } from './path-to-your-empty-directory-function'; // Adjust the import path accordingly

describe('emptyDirectory', () => {
  it('should throw an error if the specified path does not exist', async () => {
    const nonExistentPath = '/non-existent-path';
    await expect(emptyDirectory(nonExistentPath)).rejects.toThrowError(/specified path does not exist/);
  });

  it('should throw an error if the specified path is not a directory', async () => {
    const nonDirectoryPath = '/path/to/a/file.txt'; // Assuming there's a file at this path
    await expect(emptyDirectory(nonDirectoryPath)).rejects.toThrowError(/is not a directory/);
  });

  it('should empty all files and subdirectories in the specified directory', async () => {
    const tempDir = '/path/to/temp/directory'; // Create a temporary directory for testing
    // Populate the temporary directory with files and subdirectories
    // For example, you can use fs-extra to create directories and files

    await emptyDirectory(tempDir);

    // Verify that the directory is now empty
    // For example, you can check if the directory exists and if it contains any files/subdirectories
  });
});