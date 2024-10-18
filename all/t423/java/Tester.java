package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Tester {

    private static final String FILENAME = "test_file.txt";

    @Before
    public void setUp() throws IOException {
        // Setup: create a temporary file for testing.
        File file = new File(FILENAME);
        file.createNewFile();
    }

    @After
    public void tearDown() {
        // Cleanup: delete the test file after each test.
        new File(FILENAME).delete();
    }

    @Test
    public void testWriteNewLine() throws IOException {
        // Test case 1: Writing a new line to an empty file.
        String lineContent = "First unique line.";
        writeUniqueLineToFile(FILENAME, lineContent);

        try (BufferedReader reader = new BufferedReader(new FileReader(FILENAME))) {
            StringBuilder content = new StringBuilder();
            String currentLine;
            while ((currentLine = reader.readLine()) != null) {
                content.append(currentLine);
            }
            assertTrue(content.toString().contains(lineContent));
        }
    }

    @Test
    public void testWriteDuplicateLine() throws IOException {
        // Test case 2: Attempting to write a duplicate line.
        String lineContent = "First unique line.";
        // Write the line once.
        writeUniqueLineToFile(FILENAME, lineContent);
        // Attempt to write it again.
        writeUniqueLineToFile(FILENAME, lineContent);

        try (BufferedReader reader = new BufferedReader(new FileReader(FILENAME))) {
            StringBuilder content = new StringBuilder();
            String currentLine;
            while ((currentLine = reader.readLine()) != null) {
                content.append(currentLine);
            }
            assertEquals(1, content.toString().split(lineContent, -1).length - 1);
        }
    }

    @Test
    public void testWriteMultipleUniqueLines() throws IOException {
        // Test case 3: Writing multiple unique lines.
        String[] lines = {"First unique line.", "Second unique line.", "Third unique line."};
        for (String line : lines) {
            writeUniqueLineToFile(FILENAME, line);
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(FILENAME))) {
            StringBuilder content = new StringBuilder();
            String currentLine;
            while ((currentLine = reader.readLine()) != null) {
                content.append(currentLine).append("\n");
            }
            for (String line : lines) {
                assertTrue(content.toString().contains(line));
            }
        }
    }

    @Test
    public void testWriteEmptyLine() throws IOException {
        // Test case 4: Writing an empty line, should not write.
        String lineContent = "";
        writeUniqueLineToFile(FILENAME, lineContent);

        try (BufferedReader reader = new BufferedReader(new FileReader(FILENAME))) {
            StringBuilder content = new StringBuilder();
            String currentLine;
            while ((currentLine = reader.readLine()) != null) {
                content.append(currentLine);
            }
            assertEquals("", content.toString());
        }
    }

}