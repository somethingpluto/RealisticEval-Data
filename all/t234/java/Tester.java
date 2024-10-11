package org.real.temp;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class Tester {

    private StringWriter mockFile;
    private List<String[]> records;

    @BeforeEach
    public void setUp() throws IOException {
        // Set up a mock CSV file using StringWriter
        mockFile = new StringWriter();
        mockFile.write("Alice,30,USA\nBob,25,UK\nCharlie,35,Canada\n");
        records = new ArrayList<>();
        loadRecords();
    }

    private void loadRecords() throws IOException {
        // Load records from the mock file
        CSVParser parser = new CSVParser(new StringReader(mockFile.toString()), CSVFormat.DEFAULT);
        for (CSVRecord record : parser) {
            String[] row = new String[record.size()];
            for (int i = 0; i < record.size(); i++) {
                row[i] = record.get(i);
            }
            records.add(row);
        }
    }

    private void appendOrSkipRow(String[] newRow) throws IOException {
        boolean exists = false;
        for (String[] row : records) {
            // Check if the name matches (assuming first column is the name)
            if (row[0].equals(newRow[0])) {
                exists = true;
                break;
            }
        }
        // Append row only if it doesn't exist
        if (!exists) {
            records.add(newRow);
        }
        saveRecords();
    }

    private void saveRecords() {
        mockFile.getBuffer().setLength(0); // Clear the StringWriter
        for (String[] row : records) {
            mockFile.write(String.join(",", row) + "\n");
        }
    }

    @Test
    public void testAppendNewRow() throws IOException {
        // Test appending a new row when there are no matching values
        String[] newRow = {"David", "28", "Australia"};
        appendOrSkipRow(newRow);
        loadRecords(); // Reload records after appending

        boolean found = false;
        for (String[] row : records) {
            if (row[0].equals(newRow[0])) {
                found = true;
                break;
            }
        }
        assertTrue(found);
    }

    @Test
    public void testSkipDifferentValues() throws IOException {
        // Test appending a new row with different values
        String[] newRow = {"Alice", "31", "USA"}; // Same name, different age
        appendOrSkipRow(newRow);
        loadRecords(); // Reload records after appending

        boolean found = false;
        for (String[] row : records) {
            if (row[0].equals(newRow[0]) && !row[1].equals(newRow[1])) {
                found = true;
                break;
            }
        }
        assertTrue(found);
    }

    @Test
    public void testAppendRowWithDifferentColumns() throws IOException {
        // Test appending a row with different values in the first three columns
        String[] newRow = {"Eve", "40", "Australia", "Engineer"};
        appendOrSkipRow(newRow);
        loadRecords(); // Reload records after appending

        boolean found = false;
        for (String[] row : records) {
            if (row[0].equals(newRow[0])) {
                found = true;
                break;
            }
        }
        assertTrue(found);
    }

    @Test
    public void testMultipleAppends() throws IOException {
        // Test appending multiple new rows correctly
        String[][] newRows = {
            {"Frank", "29", "Germany"},
            {"Grace", "22", "France"}
        };

        for (String[] row : newRows) {
            appendOrSkipRow(row);
            loadRecords(); // Reload records after each append
        }

        for (String[] row : newRows) {
            boolean found = false;
            for (String[] existingRow : records) {
                if (existingRow[0].equals(row[0])) {
                    found = true;
                    break;
                }
            }
            assertTrue(found);
        }
    }
}
