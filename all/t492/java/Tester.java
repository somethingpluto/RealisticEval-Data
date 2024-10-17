package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Tester {

    private static final String TEST_FILE_PATH = "test_output.txt";

    @Before
    public void setUp() {
        // Set up a temporary file path for testing.
    }

    @After
    public void tearDown() {
        // Clean up the test file after each test.
        File file = new File(TEST_FILE_PATH);
        if (file.exists()) {
            file.delete();
        }
    }

    @Test
    public void testBasicContent() throws IOException {
        // Test with basic content and check if it saves correctly.
        String content = "Hello,  World!  ";
        String expected = "Hello, World!";
        saveContentToFile(content, TEST_FILE_PATH);

        try (FileReader reader = new FileReader(TEST_FILE_PATH)) {
            char[] buffer = new char[1024];
            int length = reader.read(buffer);
            String result = new String(buffer, 0, length).trim();
            assertEquals(expected, result);
        }
    }

    @Test
    public void testMultipleSpacesAndEmptyLines() throws IOException {
        // Test handling of multiple spaces and empty lines.
        String content = "\n\n\nThis is a    test.\n\nAnother line.      \n";
        String expected = "This is a test. Another line.";
        saveContentToFile(content, TEST_FILE_PATH);

        try (FileReader reader = new FileReader(TEST_FILE_PATH)) {
            char[] buffer = new char[1024];
            int length = reader.read(buffer);
            String result = new String(buffer, 0, length).trim();
            assertEquals(expected, result);
        }
    }

    @Test
    public void testOnlyWhitespace() throws IOException {
        // Test if only whitespace is handled correctly.
        String content = "    \n  \n   ";
        String expected = "";
        saveContentToFile(content, TEST_FILE_PATH);

        try (FileReader reader = new FileReader(TEST_FILE_PATH)) {
            char[] buffer = new char[1024];
            int length = reader.read(buffer);
            String result = new String(buffer, 0, length).trim();
            assertEquals(expected, result);
        }
    }

    @Test
    public void testEmptyContent() throws IOException {
        // Test if empty content is saved correctly.
        String content = "";
        String expected = "";
        saveContentToFile(content, TEST_FILE_PATH);

        try (FileReader reader = new FileReader(TEST_FILE_PATH)) {
            char[] buffer = new char[1024];
            int length = reader.read(buffer);
            String result = new String(buffer, 0, length).trim();
            assertEquals(expected, result);
        }
    }

    // Utility method to save content to a file
    private void saveContentToFile(String content, String path) {
        // Remove redundant whitespace from the content.
        // Split the content into lines, strip leading/trailing whitespace,
        // and filter out empty lines.
        content = String.join("\n",
            content.lines()
                   .filter(line -> !line.trim().isEmpty())
                   .map(String::trim)
                   .toArray(String[]::new));

        // Replace multiple spaces with a single space.
        content = content.replaceAll("\\s+", " ").trim();

        // Write the cleaned content to the specified file.
        try (FileWriter writer = new FileWriter(path, false)) {
            writer.write(content);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}