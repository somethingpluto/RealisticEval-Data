import org.junit.Before;
import org.junit.Test;

import java.io.File;

public class Tester {

    private File testDirectory;

    @Before
    public void setUp() {
        // Create a temporary directory for testing
        testDirectory = new File("tempTestDir");
        if (!testDirectory.exists()) {
            testDirectory.mkdirs();
        }
    }

    @Test(expected = IllegalArgumentException.class)
    public void testEmptyNonExistentDirectory() {
        // Test with a non-existent directory
        empty_directory("non_existent_dir");
    }

    @Test(expected = IllegalArgumentException.class)
    public void testEmptyFileInsteadOfDirectory() {
        // Test with a file instead of a directory
        File tempFile = new File(testDirectory, "testFile.txt");
        try {
            tempFile.createNewFile();
        } catch (Exception e) {
            e.printStackTrace();
        }
        empty_directory(tempFile.getAbsolutePath());
    }

    @Test
    public void testEmptyExistingDirectory() {
        // Test with an existing directory
        File subDirectory = new File(testDirectory, "subDir");
        subDirectory.mkdir();

        File testFile = new File(subDirectory, "testFile.txt");
        try {
            testFile.createNewFile();
        } catch (Exception e) {
            e.printStackTrace();
        }

        empty_directory(testDirectory.getAbsolutePath());

        // Verify that the directory is empty
        assert !subDirectory.exists() : "Subdirectory should have been deleted";
        assert !testFile.exists() : "Test file should have been deleted";
    }

    /**
     * Method to empty all files and subdirectories in the specified directory.
     *
     * @param directoryPath Path to the directory whose contents are to be emptied.
     * @throws IllegalArgumentException If the specified path does not exist or is not a directory.
     */
    public static void empty_directory(String directoryPath) throws IllegalArgumentException {
        File directory = new File(directoryPath);
        if (!directory.exists() || !directory.isDirectory()) {
            throw new IllegalArgumentException("The specified path does not exist or is not a directory.");
        }

        File[] files = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    empty_directory(file.getAbsolutePath()); // Recursively delete subdirectories
                }
                file.delete(); // Delete files
            }
        }
        directory.delete(); // Delete the main directory
    }
}