package org.real.temp;

import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import static org.junit.jupiter.api.Assertions.*;

public class Tester {

    private String inputFilePath;
    private String outputFilePath;

    @BeforeEach
    public void setUp() {
        inputFilePath = "src/test/resources/input.csv";
        outputFilePath = "src/test/resources/output.csv";
    }

    @Test
    public void testProcessCsv() throws IOException {
        // Prepare input data
        File inputFile = new File(inputFilePath);
        try (CSVWriter writer = new CSVWriter(new FileWriter(inputFile))) {
            writer.writeNext(new String[]{"col1", "col2", "col3"});
            writer.writeNext(new String[]{"value1", "", ""});
            writer.writeNext(new String[]{"", "value2", ""});
            writer.writeNext(new String[]{"value3", "value4", ""});
        }

        // Call the method under test
        ProcessCsv.processCsv(inputFilePath, outputFilePath);

        // Verify the output
        File outputFile = new File(outputFilePath);
        assertTrue(outputFile.exists());
        try (CSVReader reader = new CSVReader(new FileReader(outputFile))) {
            String[] nextLine;
            int rowCount = 0;
            while ((nextLine = reader.readNext()) != null) {
                rowCount++;
                if (rowCount == 1) { // Header row
                    assertEquals(3, nextLine.length);
                } else { // Data rows
                    assertNotEquals("", nextLine[0]);
                    assertNotEquals("", nextLine[1]);
                    assertNotEquals("", nextLine[2]);
                }
            }
            assertEquals(2, rowCount); // Only two rows should remain after processing
        }
    }
}