package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;


import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import static org.junit.Assert.assertArrayEquals;

public class Tester {

    private static final String TEST_FILE = "test_file.txt";

    @Before
    public void setUp() throws IOException {
        // Setup a temporary directory to use for each test
        File testFile = new File(TEST_FILE);
        if (!testFile.exists()) {
            testFile.createNewFile();
        }
    }

    @After
    public void tearDown() {
        // Clean up the temporary file after each test
        File testFile = new File(TEST_FILE);
        if (testFile.exists()) {
            testFile.delete();
        }
    }

    @Test
    public void testBasicFunctionality() throws IOException {
        // Test reading a file with a valid structure and numerical question
        String content = "Line 1\n" +
                "Line 2\n" +
                "/\n" +
                "1.0 2.0 3.0\n" +
                "4.0 5.0 6.0\n";

        try (FileWriter writer = new FileWriter(TEST_FILE)) {
            writer.write(content);
        }

        double[][] result = Answer.readColumns(TEST_FILE);
        double[][] expectedResult = {
                {1.0, 2.0, 3.0},
                {4.0, 5.0, 6.0}
        };

        assertArrayEquals(expectedResult, result);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNoSlashCharacter() throws IOException {
        // Test that an IllegalArgumentException is raised if no '/' character is found
        String content = "Line 1\n" +
                "Line 2\n" +
                "Line 3\n";

        try (FileWriter writer = new FileWriter(TEST_FILE)) {
            writer.write(content);
        }

        Answer.readColumns(TEST_FILE);
    }

    @Test
    public void testFileWithCommentsAndEmptyLines() throws IOException {
        // Test handling of comments and empty lines
        String content = "Line 1\n" +
                "/\n" +
                "! This is a comment\n" +
                "1.0 2.0 3.0\n" +
                "\n" +
                "4.0 5.0 6.0\n" +
                "! Another comment\n";

        try (FileWriter writer = new FileWriter(TEST_FILE)) {
            writer.write(content);
        }

        double[][] result = Answer.readColumns(TEST_FILE);
        double[][] expectedResult = {
                {1.0, 2.0, 3.0},
                {4.0, 5.0, 6.0}
        };

        assertArrayEquals(expectedResult, result);
    }
}