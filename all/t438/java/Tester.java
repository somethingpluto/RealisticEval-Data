package org.real.temp;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvValidationException;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;

import java.io.*;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for reading a CSV file and converting it to a List of Lists representing a DataFrame.
 */
public class Tester {

    private Path tempFile;

    @BeforeEach
    public void setup(@TempDir Path tempDir) throws IOException {
        tempFile = tempDir.resolve("test.csv");
        try (PrintWriter writer = new PrintWriter(tempFile.toFile())) {
            writer.println("col1,col2,col3");
            writer.println("1,2,3");
            writer.println("4,5,6");
        }
    }

    @Test
    public void testReadCsvToDataFrame() throws IOException, CsvValidationException {
        List<List<String>> expected = new ArrayList<>();
        expected.add(List.of("col1", "col2", "col3"));
        expected.add(List.of("1", "2", "3"));
        expected.add(List.of("4", "5", "6"));

        List<List<String>> actual = Answer.readCsvToDataFrame(tempFile.toString());

        assertEquals(expected.size(), actual.size(), "The number of rows should match.");

        for (int i = 0; i < expected.size(); i++) {
            List<String> expectedRow = expected.get(i);
            List<String> actualRow = actual.get(i);

            assertEquals(expectedRow.size(), actualRow.size(), "The number of columns should match for row " + i);

            for (int j = 0; j < expectedRow.size(); j++) {
                assertEquals(expectedRow.get(j), actualRow.get(j), "Values should match at position (" + i + ", " + j + ")");
            }
        }
    }

    @Test
    public void testReadCsvToDataFrameFileNotFound() {
        String nonExistentFilePath = "non-existent-file.csv";

        List<List<String>> result = Answer.readCsvToDataFrame(nonExistentFilePath);

        assertNull(result, "The result should be null if the file is not found.");
    }

    @Test
    public void testReadCsvToDataFrameEmptyFile() throws IOException {
        Path emptyFile = tempFile.resolveSibling("empty.csv");
        try (PrintWriter writer = new PrintWriter(emptyFile.toFile())) {
            // Write nothing to create an empty file
        }

        List<List<String>> result = Answer.readCsvToDataFrame(emptyFile.toString());

        assertNotNull(result, "The result should not be null.");
        assertTrue(result.isEmpty(), "The result should be an empty list for an empty file.");
    }
}