package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;
import org.real.temp.Answer;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Tester {

    // Test case 1: Basic find and replace
    @Test
    public void testFindAndReplaceBasic(@TempDir Path tempDir) throws IOException {
        Path filePath = tempDir.resolve("testfile.txt");
        Files.write(filePath, List.of("Hello World", "Goodbye World"));

        Answer.findAndReplaceInFile(filePath, "World", "Java");

        List<String> result = Files.readAllLines(filePath);
        assertEquals(List.of("Hello Java", "Goodbye Java"), result);
    }

    // Test case 2: No occurrences of the search string
    @Test
    public void testFindAndReplaceNoOccurrences(@TempDir Path tempDir) throws IOException {
        Path filePath = tempDir.resolve("testfile.txt");
        Files.write(filePath, List.of("Hello World", "Goodbye World"));

        Answer.findAndReplaceInFile(filePath, "Python", "Java");

        List<String> result = Files.readAllLines(filePath);
        assertEquals(List.of("Hello World", "Goodbye World"), result);
    }

    // Test case 3: Multiple occurrences in a single line
    @Test
    public void testFindAndReplaceMultipleOccurrences(@TempDir Path tempDir) throws IOException {
        Path filePath = tempDir.resolve("testfile.txt");
        Files.write(filePath, List.of("Hello World World", "Goodbye World"));

        Answer.findAndReplaceInFile(filePath, "World", "Java");

        List<String> result = Files.readAllLines(filePath);
        assertEquals(List.of("Hello Java Java", "Goodbye Java"), result);
    }

    // Test case 4: Replace with an empty string
    @Test
    public void testFindAndReplaceWithEmptyString(@TempDir Path tempDir) throws IOException {
        Path filePath = tempDir.resolve("testfile.txt");
        Files.write(filePath, List.of("Hello World", "Goodbye World"));

        Answer.findAndReplaceInFile(filePath, "World", "");

        List<String> result = Files.readAllLines(filePath);
        assertEquals(List.of("Hello ", "Goodbye "), result);
    }

    // Test case 5: Empty file
    @Test
    public void testFindAndReplaceEmptyFile(@TempDir Path tempDir) throws IOException {
        Path filePath = tempDir.resolve("testfile.txt");
        Files.write(filePath, List.of(""));

        Answer.findAndReplaceInFile(filePath, "World", "Java");

        List<String> result = Files.readAllLines(filePath);
        assertEquals(List.of(""), result);
    }

}
