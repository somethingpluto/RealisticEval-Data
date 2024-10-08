package org.real.temp;

import org.junit.jupiter.api.*;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class Tester {
    private Answer answer;
    private final String testFilePath = "test_output.csv"; // Path for test output file

    @BeforeEach
    public void setUp() {
        answer = new Answer(); // Create an instance of the Answer class
    }

    @AfterEach
    public void tearDown() throws IOException {
        // Delete the test file after each test
        Path path = Paths.get(testFilePath);
        if (Files.exists(path)) {
            Files.delete(path);
        }
    }

    @Test
    public void testWriteCsvToFile_WithMultipleStrings() {
        List<String> data = List.of("Apple", "Banana", "Cherry");
        answer.writeCsvToFile(data, testFilePath);

        // Assert the content of the file
        String content = readFile(testFilePath);
        assertEquals("Apple,Banana,Cherry", content);
    }

    @Test
    public void testWriteCsvToFile_WithSingleString() {
        List<String> data = List.of("Apple");
        answer.writeCsvToFile(data, testFilePath);

        // Assert the content of the file
        String content = readFile(testFilePath);
        assertEquals("Apple", content);
    }

    @Test
    public void testWriteCsvToFile_WithEmptyList() {
        List<String> data = List.of();
        answer.writeCsvToFile(data, testFilePath);

        // Assert the content of the file is empty
        String content = readFile(testFilePath);
        assertEquals("", content);
    }


    @Test
    public void testWriteCsvToFile_WithSpecialCharacters() {
        List<String> data = List.of("Apple", "Banana, Cherry", "Date");
        answer.writeCsvToFile(data, testFilePath);

        // Assert the content of the file
        String content = readFile(testFilePath);
        assertEquals("Apple,Banana, Cherry,Date", content);
    }

    @Test
    public void testWriteCsvToFile_WithSpaces() {
        List<String> data = List.of("Apple ", " Banana", " Cherry ");
        answer.writeCsvToFile(data, testFilePath);

        // Assert the content of the file with spaces
        String content = readFile(testFilePath);
        assertEquals("Apple , Banana, Cherry ", content);
    }

    @Test
    public void testWriteCsvToFile_WithFileOverwrite() {
        // First write to the file
        List<String> firstData = List.of("Apple", "Banana");
        answer.writeCsvToFile(firstData, testFilePath);

        // Now overwrite with new data
        List<String> secondData = List.of("Cherry", "Date");
        answer.writeCsvToFile(secondData, testFilePath);

        // Assert that the file now contains the new data
        String content = readFile(testFilePath);
        assertEquals("Cherry,Date", content);
    }

    // Helper method to read file content as a String
    private String readFile(String filePath) {
        try {
            return Files.readString(Path.of(filePath));
        } catch (IOException e) {
            fail("Failed to read file: " + e.getMessage());
            return "";
        }
    }
}