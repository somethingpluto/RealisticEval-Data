package org.real.temp;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import org.real.temp.*;

public class Tester {
    private File sourceFile;
    private File destinationFile;

    @Before
    public void setUp() throws IOException {
        sourceFile = new File("testSourceFile.txt");
        destinationFile = new File("testDestinationFile.txt");

        try (FileOutputStream fos = new FileOutputStream(sourceFile)) {
            fos.write("This is a test file content.".getBytes());
        }
    }

    @After
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
        assertTrue("Destination file should exist after copying.", destinationFile.exists());
        assertEquals("File sizes should match.", sourceFile.length(), destinationFile.length());
        assertTrue("Time taken should be non-negative.", timeTaken >= 0);
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
        assertTrue("Destination file should exist after copying.", destinationEmptyFile.exists());
        assertEquals("Empty file should have length 0.", 0, destinationEmptyFile.length());
        assertTrue("Time taken should be non-negative.", timeTaken >= 0);

        emptyFile.delete();
        destinationEmptyFile.delete();
    }

    /**
     * Test copying a non-existent source file.
     */
    @Test(expected = IOException.class)
    public void testCopyNonExistentFile() throws IOException {
        String nonExistentFilePath = "nonExistentFile.txt";
        Answer.copyFileWithBufferedStream(nonExistentFilePath, destinationFile.getAbsolutePath());
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
        assertTrue("Destination file should exist after copying.", destinationFile.exists());
        assertEquals("File sizes should match after overwriting.", sourceFile.length(), destinationFile.length());
        assertTrue("Time taken should be greater than 0.", timeTaken > 0);
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
        assertTrue("Destination file should exist after copying.", destinationFile.exists());
        assertEquals("File sizes should match.", sourceFile.length(), destinationFile.length());
        assertTrue("Time taken should be greater than 0.", timeTaken > 0);
    }
}
