package org.real.temp;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import static org.junit.jupiter.api.Assertions.*;


import org.real.temp.*;
public class Tester {

    private File testFile;

    @BeforeEach
    public void setUp() throws IOException {
        testFile = new File("testFile.txt");
        try (FileOutputStream fos = new FileOutputStream(testFile)) {
            fos.write("Test content".getBytes());
        }
    }

    @AfterEach
    public void tearDown() {
        if (testFile.exists()) {
            testFile.delete();
        }
    }

    /**
     * Test reading a file that exists and has content.
     */
    @Test
    public void testReadFileWithContent() throws IOException {
        byte[] content = Adapted.readFileToByteArray(testFile.getAbsolutePath());
        assertEquals("Test content", new String(content), "The file content should match the expected string.");
    }

    /**
     * Test reading an empty file.
     */
    @Test
    public void testReadEmptyFile() throws IOException {
        File emptyFile = new File("emptyFile.txt");
        emptyFile.createNewFile();

        byte[] content = Adapted.readFileToByteArray(emptyFile.getAbsolutePath());
        assertEquals(0, content.length, "The content of an empty file should be a byte array of length 0.");

        emptyFile.delete();
    }

    /**
     * Test reading a file that does not exist.
     */
    @Test
    public void testReadNonExistentFile() {
        String nonExistentFilePath = "nonExistentFile.txt";
        assertThrows(IllegalArgumentException.class, () -> {
            Adapted.readFileToByteArray(nonExistentFilePath);
        }, "Reading a non-existent file should throw an IllegalArgumentException.");
    }

    /**
     * Test reading a file with special characters in its content.
     */
    @Test
    public void testReadFileWithSpecialCharacters() throws IOException {
        String specialContent = "Special content: !@#$%^&*()_+";
        try (FileOutputStream fos = new FileOutputStream(testFile)) {
            fos.write(specialContent.getBytes());
        }

        byte[] content = Adapted.readFileToByteArray(testFile.getAbsolutePath());
        assertEquals(specialContent, new String(content), "The file content should match the special characters string.");
    }

    /**
     * Test reading a large file.
     */
    @Test
    public void testReadLargeFile() throws IOException {
        byte[] largeContent = new byte[10 * 1024 * 1024]; // 10 MB
        for (int i = 0; i < largeContent.length; i++) {
            largeContent[i] = (byte) (i % 256);
        }

        try (FileOutputStream fos = new FileOutputStream(testFile)) {
            fos.write(largeContent);
        }

        byte[] content = Adapted.readFileToByteArray(testFile.getAbsolutePath());
        assertArrayEquals(largeContent, content, "The content of the large file should match the expected byte array.");
    }
}
