package com.real.t179;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

import static org.junit.jupiter.api.Assertions.*;

import com.real.t179.Adapted.*;
public class TestClass {
    private File sourceDir;
    private File targetDir;

    @BeforeEach
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

    @AfterEach
    public void tearDown() {
        deleteDirectory(sourceDir);
        deleteDirectory(targetDir);
    }

    /**
     * Test copying an empty directory.
     */
    @Test
    public void testCopyEmptyDirectory() throws IOException {
        Adapted.copyDirectory(sourceDir, targetDir);
        assertTrue(targetDir.exists(), "Target directory should exist after copying.");
        assertTrue(targetDir.isDirectory(), "Target directory should be a directory.");
        assertEquals(0, targetDir.listFiles().length, "Target directory should be empty.");
    }

    /**
     * Test copying a directory with files.
     */
    @Test
    public void testCopyDirectoryWithFiles() throws IOException {
        File testFile = new File(sourceDir, "testFile.txt");
        Files.createFile(testFile.toPath());

        Adapted.copyDirectory(sourceDir, targetDir);
        File copiedFile = new File(targetDir, "testFile.txt");

        assertTrue(copiedFile.exists(), "File should be copied to target directory.");
        assertEquals(testFile.length(), copiedFile.length(), "File size should be the same after copying.");
    }

    /**
     * Test handling of non-existent source directory.
     */
    @Test
    public void testNonExistentSourceDirectory() {
        File nonExistentDir = new File("nonExistentDir");
        IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () ->
            Adapted.copyDirectory(nonExistentDir, targetDir), "Expected exception for non-existent source directory.");

        assertTrue(exception.getMessage().contains("Source directory does not exist"), "Exception message should indicate non-existent source directory.");
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

        Adapted.copyDirectory(sourceDir, targetDir);
        File copiedSubDir = new File(targetDir, "subDir");
        File copiedFile = new File(copiedSubDir, "testFile.txt");

        assertTrue(copiedSubDir.exists(), "Subdirectory should be copied to target directory.");
        assertTrue(copiedFile.exists(), "File within subdirectory should be copied to target directory.");
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
        Adapted.copyDirectory(sourceDir, targetDir);
        File copiedFile = new File(targetDir, "testFile.txt");

        assertTrue(copiedFile.exists(), "File should be copied to target directory.");

        // Check that the content of the file is now the same as the source file
        String copiedContent = Files.readString(copiedFile.toPath());
        assertEquals("Source content", copiedContent, "File in target directory should be overwritten with source content.");
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
