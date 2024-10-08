package org.real.temp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.AfterEach;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
public class Tester {

    private final Answer answer = new Answer();
    private final String testFilePath = "test.csv";

    @BeforeEach
    public void setUp() throws IOException {
        // Create a temporary CSV file for testing
        // Writing sample CSV content to the file
        String sampleCsvContent = "Name,Age,Location\n" +
                "Alice,30,New York\n" +
                "Bob,25,Los Angeles\n" +
                "Charlie,35,Chicago\n";
        Files.write(Paths.get(testFilePath), sampleCsvContent.getBytes(), StandardOpenOption.CREATE);
    }

    @Test
    public void testReadValidCsv() throws IOException {
        List<List<String>> result = answer.readCsv(testFilePath);
        assertEquals(4, result.size()); // 4 lines including the header
        assertEquals(List.of("Name", "Age", "Location"), result.get(0)); // Check header
        assertEquals(List.of("Alice", "30", "New York"), result.get(1));
        assertEquals(List.of("Bob", "25", "Los Angeles"), result.get(2));
        assertEquals(List.of("Charlie", "35", "Chicago"), result.get(3));
    }

    @Test
    public void testReadEmptyCsv() throws IOException {
        // Create an empty CSV file
        Files.write(Paths.get(testFilePath), "".getBytes(), StandardOpenOption.TRUNCATE_EXISTING);
        List<List<String>> result = answer.readCsv(testFilePath);
        assertTrue(result.isEmpty()); // Expecting an empty list
    }


    @Test
    public void testReadCsvWithQuotes() throws IOException {
        // Write CSV content with quoted fields
        String contentWithQuotes = "\"Name\",\"Age\",\"Location\"\n" +
                "\"Alice\",\"30\",\"New York\"\n" +
                "\"Bob\",\"25\",\"Los Angeles\"\n";
        Files.write(Paths.get(testFilePath), contentWithQuotes.getBytes(), StandardOpenOption.TRUNCATE_EXISTING);
        List<List<String>> result = answer.readCsv(testFilePath);
        assertEquals(3, result.size()); // 3 lines including the header
        assertEquals(List.of("\"Name\"", "\"Age\"", "\"Location\""), result.get(0));
    }

    @Test
    public void testReadInvalidCsvFile() {
        // Attempt to read a non-existent file and assert that a FileNotFoundException is thrown
        assertThrows(Exception.class, () -> {
            answer.readCsv("non_existent_file.csv");
        });
    }

    @Test
    public void testReadCsvWithDifferentDelimiters() throws IOException {
        // Write CSV content with semicolons instead of commas
        String contentWithSemicolons = "Name;Age;Location\n" +
                "Alice;30;New York\n" +
                "Bob;25;Los Angeles\n";
        Files.write(Paths.get(testFilePath), contentWithSemicolons.getBytes(), StandardOpenOption.TRUNCATE_EXISTING);
        // Modify the readCsv function to handle semicolons if necessary.
        List<List<String>> result = answer.readCsv(testFilePath);
        assertEquals(3, result.size()); // Expecting 3 lines
        assertEquals(List.of("Name;Age;Location"), result.get(0));
    }

    // Clean up after tests (Optional)
    @AfterEach
    public void tearDown() throws IOException {
        Files.deleteIfExists(Paths.get(testFilePath)); // Remove test file after tests
    }
}
