package org.real.temp;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;
import static org.real.temp.Answer.*;
public class Tester {
    private File testFile;

    @Before
    public void setUp() throws IOException {
        // Create a temporary file for testing
        testFile = new File("test_file.txt");
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(testFile))) {
            writer.write("Line 1\n");
            writer.write("Line 2\n");
            writer.write("Line 3\n");
        }
    }

    @After
    public void tearDown() {
        // Remove the temporary file after testing
        if (testFile.exists()) {
            testFile.delete();
        }
    }

    @Test
    public void testPrependString() throws IOException {
        // Test appending a simple string to the beginning of each line
        prependToEachLine(testFile.getAbsolutePath(), "Test: ");
        assertLinesEqual(new String[]{
                "Test: Line 1",
                "Test: Line 2",
                "Test: Line 3"
        });
    }

    @Test
    public void testPrependEmptyString() throws IOException {
        // Test appending an empty string
        prependToEachLine(testFile.getAbsolutePath(), "");
        assertLinesEqual(new String[]{
                "Line 1",
                "Line 2",
                "Line 3"
        });
    }

    @Test
    public void testPrependSpecialCharacters() throws IOException {
        // Test appending special characters to the beginning of each line
        prependToEachLine(testFile.getAbsolutePath(), "#$%^&* ");
        assertLinesEqual(new String[]{
                "#$%^&* Line 1",
                "#$%^&* Line 2",
                "#$%^&* Line 3"
        });
    }

    @Test
    public void testPrependNumericString() throws IOException {
        // Test appending numeric string to the beginning of each line
        prependToEachLine(testFile.getAbsolutePath(), "123 ");
        assertLinesEqual(new String[]{
                "123 Line 1",
                "123 Line 2",
                "123 Line 3"
        });
    }

    @Test
    public void testFileNotFound() {
        // Test the response when the file does not exist
        try {
            prependToEachLine("non_existent_file.txt", "Test: ");
            fail("Expected IOException to be thrown");
        } catch (Exception e) {
            // Expected exception
        }
    }

    private void assertLinesEqual(String[] expected) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(testFile))) {
            String[] actual = reader.lines().toArray(String[]::new);
            assertArrayEquals(expected, actual);
        }
    }

}
