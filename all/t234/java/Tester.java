package org.real.temp;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import org.junit.Before;
import org.junit.Test;

public class Tester {

    private String filePath = "test.csv";

    @Before
    public void setUp() throws IOException {
        // Create a temporary CSV file for testing
        BufferedWriter writer = new BufferedWriter(new FileWriter(filePath));
        writer.write("col1,col2,col3,col4\n");
        writer.write("value1,value2,value3,value4\n");
        writer.close();
    }

    @Test
    public void testAppendOrSkipRow() throws IOException {
        // Open the CSV file in read-plus mode
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        BufferedWriter writer = new BufferedWriter(new FileWriter(filePath, true));

        // Define a candidate row to append
        List<String> rowCandidate = Arrays.asList("value5", "value6", "value7", "value8");

        // Call the method under test
        appendOrSkipRow(writer, reader, rowCandidate);

        // Close resources
        reader.close();
        writer.close();

        // Verify that the new row was appended
        BufferedReader verifier = new BufferedReader(new FileReader(filePath));
        String line;
        boolean found = false;
        while ((line = verifier.readLine()) != null) {
            if (line.equals("value5,value6,value7,value8")) {
                found = true;
                break;
            }
        }
        verifier.close();

        assertTrue("The row should have been appended", found);
    }

    private void appendOrSkipRow(BufferedWriter writer, BufferedReader reader, List<String> rowCandidate) throws IOException {
        String[] existingRows = reader.lines().toArray(String[]::new);
        boolean skip = false;

        for (String existingRow : existingRows) {
            String[] cols = existingRow.split(",");
            if (cols[0].equals(rowCandidate.get(0)) &&
                cols[1].equals(rowCandidate.get(1)) &&
                cols[2].equals(rowCandidate.get(2))) {
                skip = true;
                break;
            }
        }

        if (!skip) {
            writer.newLine();
            writer.write(String.join(",", rowCandidate));
        }
    }
}