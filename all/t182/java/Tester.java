package org.real.temp;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

import org.real.temp.*;

public class Tester {
    private File sourceFile;
    private File destinationFile;

    @BeforeEach
    public void setUp() throws IOException {
        sourceFile = new File("testSourceFile.txt");
        destinationFile = new File("testDestinationFile.txt");

        try (FileOutputStream fos = new FileOutputStream(sourceFile)) {
            fos.write("This is a test file content.".getBytes());
        }
    }

    @AfterEach
    public void tearDown() {
        if (sourceFile.exists()) {
            sourceFile.delete();
        }
        if (destinationFile.exists()) {
            destinationFile.delete();
        }
    }

    /**
     * Test copying a file with content.
     */
    @Test
    public void testCopyFileWithContent() throws IOException {
        long timeTaken = Answer.copyFileWithBufferedStream(sourceFile.getAbsolutePath(), destinationFile.getAbsolutePath());
        assertTrue(destinationFile.exists(), "Destination file should exist after copying.");
        assertEquals(sourceFile.length(), destinationFile.length(), "File sizes should match.");
        assertTrue(timeTaken >= 0, "Time taken should be non-negative.");
    }

    /**
     * Test copying an empty file.
     */
    @Test
    public void testCopyEmptyFile() throws IOException {
        File emptyFile = new File("emptyFile.txt");
        emptyFile.createNewFile();
        File destinationEmptyFile = new File("destinationEmptyFile.txt");

        long timeTaken = Answer.copyFileWithBufferedStream(emptyFile.getAbsolutePath(), destinationEmptyFile.getAbsolutePath());
        assertTrue(destinationEmptyFile.exists(), "Destination file should exist after copying.");
        assertEquals(0, destinationEmptyFile.length(), "Empty file should have length 0.");
        assertTrue(timeTaken >= 0, "Time taken should be non-negative.");

        emptyFile.delete();
        destinationEmptyFile.delete();
    }

    /**
     * Test copying a non-existent source file.
     */
    @Test
    public void testCopyNonExistentFile() {
        String nonExistentFilePath = "nonExistentFile.txt";
        assertThrows(IOException.class, () -> {
            Answer.copyFileWithBufferedStream(nonExistentFilePath, destinationFile.getAbsolutePath());
        }, "Copying a non-existent file should throw an IOException.");
    }

    /**
     * Test copying a file to an existing destination file (overwriting).
     */
    @Test
    public void testCopyFileOverwrite() throws IOException {
        try (FileOutputStream fos = new FileOutputStream(destinationFile)) {
            fos.write("Old content".getBytes());
        }

        long timeTaken = Answer.copyFileWithBufferedStream(sourceFile.getAbsolutePath(), destinationFile.getAbsolutePath());
        assertTrue(destinationFile.exists(), "Destination file should exist after copying.");
        assertEquals(sourceFile.length(), destinationFile.length(), "File sizes should match after overwriting.");
        assertTrue(timeTaken > 0, "Time taken should be greater than 0.");
    }

    /**
     * Test copying a large file.
     */
    @Test
    public void testCopyLargeFile() throws IOException {
        byte[] largeContent = new byte[10 * 1024 * 1024]; // 10 MB
        for (int i = 0; i < largeContent.length; i++) {
            largeContent[i] = (byte) (i % 256);
        }

        try (FileOutputStream fos = new FileOutputStream(sourceFile)) {
            fos.write(largeContent);
        }

        long timeTaken = Answer.copyFileWithBufferedStream(sourceFile.getAbsolutePath(), destinationFile.getAbsolutePath());
        assertTrue(destinationFile.exists(), "Destination file should exist after copying.");
        assertEquals(sourceFile.length(), destinationFile.length(), "File sizes should match.");
        assertTrue(timeTaken > 0, "Time taken should be greater than 0.");
    }
}
