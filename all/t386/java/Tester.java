package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;



import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import static org.real.temp.Answer.*;

public class Tester {

    private String testDir = "test_files";
    private String inputFilePath;
    private String outputFilePath;

    @Before
    public void setUp() throws IOException {
        // Create a directory for test files if it doesn't exist
        File dir = new File(testDir);
        dir.mkdirs();
        inputFilePath = new File(testDir, "test_input.txt").getAbsolutePath();
        outputFilePath = new File(testDir, "test_output.txt").getAbsolutePath();
    }

    @After
    public void tearDown() {
        // Remove test directory and all created files after each test
        File dir = new File(testDir);
        if (dir.exists()) {
            deleteDirectory(dir);
        }
    }

    private void writeToFile(String filePath, String text, String encoding) throws IOException {
        // Helper method to write text to a file with a specific encoding
        try (FileWriter writer = new FileWriter(filePath, StandardCharsets.UTF_8)) {
            writer.write(text);
        }
    }

    @Test
    public void testBasicConversion() throws IOException {
        // Test basic conversion from cp932 to utf_16
        writeToFile(inputFilePath, "これはテストです", "cp932");
        boolean result = convertEncoding(inputFilePath, outputFilePath,"cp932","utf_16");
        assertTrue(result);
        String content = readFile(outputFilePath, "utf_16");
        assertEquals("これはテストです", content);
    }


    

    @Test
    public void testOutputAlreadyConverted() throws IOException {
        // Test behavior when file is already in target encoding and copied directly
        writeToFile(inputFilePath, "Already utf_16", "utf_16");
        boolean result = convertEncoding(inputFilePath, outputFilePath, "cp932", "utf_16");
        assertTrue(result);
    }



    private String readFile(String filePath, String encoding) throws IOException {
        // Helper method to read text from a file with a specific encoding
        StringBuilder contentBuilder = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                contentBuilder.append(line).append(System.lineSeparator());
            }
        }
        return contentBuilder.toString();
    }

    private void deleteDirectory(File directory) {
        File[] files = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    deleteDirectory(file);
                } else {
                    file.delete();
                }
            }
        }
        directory.delete();
    }
}