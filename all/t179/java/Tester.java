package org.real.temp;

import org.junit.Test;
import org.junit.After;
import org.junit.Before;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

import static org.junit.Assert.*; // Changed from org.junit.jupiter.api.Assertions to org.junit.Assert

import org.real.temp.Answer.*;

public class Tester {
    private File sourceDir;
    private File targetDir;

    @Before
    public void setUp() throws IOException {
        sourceDir = new File("testSourceDir");
        targetDir = new File("testTargetDir");

        if (!sourceDir.exists()) {
            sourceDir.mkdir();
        }

        if (!targetDir.exists()) {
            targetDir.mkdir();
        }
    }

    @After
    public void tearDown() {
        deleteDirectory(sourceDir);
        deleteDirectory(targetDir);
    }

    /**
     * Test copying an empty directory.
     */
    @Test
    public void testCopyEmptyDirectory() throws IOException {
        Answer.copyDirectory(sourceDir, targetDir);
        assertTrue("Target directory should exist after copying.", targetDir.exists());
        assertTrue("Target directory should be a directory.", targetDir.isDirectory());
        assertEquals("Target directory should be empty.", 0, targetDir.listFiles().length);
    }

    /**
     * Test copying a directory with files.
     */
    @Test
    public void testCopyDirectoryWithFiles() throws IOException {
        File testFile = new File(sourceDir, "testFile.txt");
        Files.createFile(testFile.toPath());

        Answer.copyDirectory(sourceDir, targetDir);
        File copiedFile = new File(targetDir, "testFile.txt");

        assertTrue("File should be copied to target directory.", copiedFile.exists());
        assertEquals("File size should be the same after copying.", testFile.length(), copiedFile.length());
    }

    /**
     * Test handling of non-existent source directory.
     */
    @Test(expected = Exception.class) // Changed to expected for JUnit 4
    public void testNonExistentSourceDirectory() throws IOException {
        File nonExistentDir = new File("nonExistentDir");
        Answer.copyDirectory(nonExistentDir, targetDir); // No need for assertThrows
    }

    /**
     * Test copying a directory with subdirectories.
     */
    @Test
    public void testCopyDirectoryWithSubdirectories() throws IOException {
        File subDir = new File(sourceDir, "subDir");
        subDir.mkdir();
        File testFile = new File(subDir, "testFile.txt");
        Files.createFile(testFile.toPath());

        Answer.copyDirectory(sourceDir, targetDir);
        File copiedSubDir = new File(targetDir, "subDir");
        File copiedFile = new File(copiedSubDir, "testFile.txt");

        assertTrue("Subdirectory should be copied to target directory.", copiedSubDir.exists());
        assertTrue("File within subdirectory should be copied to target directory.", copiedFile.exists());
    }

    /**
     * Test overwriting files in the target directory.
     */
    @Test
    public void testOverwriteFileInTargetDirectory() throws IOException {
        // Create a source file with some content
        File testFile = new File(sourceDir, "testFile.txt");
        Files.writeString(testFile.toPath(), "Source content");

        // Create a target file with different content
        File targetFile = new File(targetDir, "testFile.txt");
        Files.writeString(targetFile.toPath(), "Target content");

        // Copy the directory, which should overwrite the target file
        Answer.copyDirectory(sourceDir, targetDir);
        File copiedFile = new File(targetDir, "testFile.txt");

        assertTrue("File should be copied to target directory.", copiedFile.exists());

        // Check that the content of the file is now the same as the source file
        String copiedContent = Files.readString(copiedFile.toPath());
        assertEquals("File in target directory should be overwritten with source content.", "Source content", copiedContent);
    }

    /**
     * Helper method to delete a directory and its contents.
     *
     * @param dir The directory to delete.
     */
    private void deleteDirectory(File dir) {
        File[] files = dir.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    deleteDirectory(file);
                } else {
                    file.delete();
                }
            }
        }
        dir.delete();
    }
}
