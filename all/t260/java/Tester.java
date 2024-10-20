package org.real.temp;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVPrinter;
import org.apache.commons.csv.CSVRecord;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import static org.real.temp.Answer.*;
/**
 * Test class for the processCsv function.
 */
public class Tester {

    private String input_data_1 = "A,B,C\n1,2,3\n4,,6\n7,8,\n9,10,11";
    private String input_data_2 = "A,B,C,D\n,,\n1,,3,4\n2,3,,5\n,,,\n";
    private String input_data_3 = "A\n1\n2\n3";

    private String inputFilePath = "input.csv";
    private String outputFilePath = "output.csv";

    @Before
    public void setUp() throws IOException {
        // Write input data to a temporary CSV file
        Files.write(Paths.get(inputFilePath), input_data_1.getBytes());
    }

    @After
    public void tearDown() throws IOException {
        // Clean up temp files
        Files.deleteIfExists(Paths.get(inputFilePath));
        Files.deleteIfExists(Paths.get(outputFilePath));
    }

    private String processData(String input_data) throws IOException {
        // Write input data to a temp CSV file
        Files.write(Paths.get(inputFilePath), input_data.getBytes());

        // Process the CSV
        processCsv(inputFilePath, outputFilePath);

        // Read the output
        String output_data = new String(Files.readAllBytes(Paths.get(outputFilePath)));

        // Clean up temp files
        Files.deleteIfExists(Paths.get(inputFilePath));
        Files.deleteIfExists(Paths.get(outputFilePath));

        return output_data;
    }

    @Test
    public void testCase1() throws IOException {
        String output = processData(input_data_1);
        String expectedOutput = "A,B,C\n1,2.0,3.0\n4,,6.0\n7,8.0,\n9,10.0,11.0\n";
        assertEquals(expectedOutput, output);
    }

    @Test
    public void testCase2() throws IOException {
        String output = processData(input_data_2);
        String expectedOutput = "A,B,C,D\n1.0,,3.0,4.0\n2.0,3.0,,5.0\n";
        assertEquals(expectedOutput, output);
    }

    @Test
    public void testCase3() throws IOException {
        String output = processData(input_data_3);
        String expectedOutput = "A\n1\n2\n3\n";  // Single-column CSV should remain unchanged
        assertEquals(expectedOutput, output);
    }

}