package org.real.temp;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

class Tester {

    private String testFilePath;

    @BeforeEach
    void setUp() throws IOException {
        // Create a temporary file for testing
        testFilePath = "testFile.txt";
        File file = new File(testFilePath);
        file.createNewFile();
    }

    // Helper method to write to the test file
    private void writeToFile(String content) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(testFilePath))) {
            writer.write(content);
        }
    }

    @Test
    void testNormalInput() throws IOException {
        writeToFile("Line 1\nLine 2 # Comment\nLine 3\n");
        List<String> result = readFileAndProcessLines(testFilePath);
        assertEquals(List.of("Line 1", "Line 2", "Line 3"), result);
    }

    @Test
    void testOnlyComments() throws IOException {
        writeToFile("# This is a comment\n# Another comment\n");
        List<String> result = readFileAndProcessLines(testFilePath);
        assertEquals(List.of(), result);
    }

    @Test
    void testEmptyLines() throws IOException {
        writeToFile("Line 1\n\nLine 2\n\n\nLine 3 # Comment\n");
        List<String> result = readFileAndProcessLines(testFilePath);
        assertEquals(List.of("Line 1", "Line 2", "Line 3"), result);
    }

    @Test
    void testNoInlineComments() throws IOException {
        writeToFile("Line 1\nLine 2\nLine 3\n");
        List<String> result = readFileAndProcessLines(testFilePath);
        assertEquals(List.of("Line 1", "Line 2", "Line 3"), result);
    }


    @Test
    void testOnlyNewLines() throws IOException {
        writeToFile("\n\n\n\n");
        List<String> result = readFileAndProcessLines(testFilePath);
        assertEquals(List.of(), result);
    }

    @Test
    void testMixedContent() throws IOException {
        writeToFile("Valid line\n# This is a comment\nLine 2\n# Another comment\n\nLine 3 # End of line comment\n");
        List<String> result = readFileAndProcessLines(testFilePath);
        assertEquals(List.of("Valid line", "Line 2", "Line 3"), result);
    }

    // Cleanup after tests
    @AfterEach
    void tearDown() throws IOException {
        Files.deleteIfExists(Paths.get(testFilePath));
    }

    // The method to be tested
    public List<String> readFileAndProcessLines(String path) {
        List<String> processedLines = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
            String line;

            while ((line = reader.readLine()) != null) {
                // Remove inline comments
                line = line.split("#")[0].trim();
                // Only add non-empty lines to the list
                if (!line.isEmpty()) {
                    processedLines.add(line);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
            throw new IllegalArgumentException("Error reading file: " + e.getMessage());
        }

        return processedLines;
    }
}
