package org.real.temp;

import org.junit.jupiter.api.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.*;

public class Tester {

    private static final String TEST_FILE = "testFile.txt";
    private Answer answer;

    @BeforeEach
    public void setUp() throws IOException {
        answer = new Answer();
        // Create a test file with initial content
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(TEST_FILE))) {
            writer.write("Line 1");
            writer.newLine();
            writer.write("Line 2");
            writer.newLine();
            writer.write("Line 3");
            writer.newLine();
        }
    }

    @AfterEach
    public void tearDown() throws IOException {
        // Clean up the test file after each test
        Files.deleteIfExists(Paths.get(TEST_FILE));
    }

    @Test
    public void testModifyLine_Success() throws IOException {
        answer.modifyLineInFile(TEST_FILE, 2, "Updated Line 2");
        try (BufferedReader reader = new BufferedReader(new FileReader(TEST_FILE))) {
            assertEquals("Line 1", reader.readLine());
            assertEquals("Updated Line 2", reader.readLine());
            assertEquals("Line 3", reader.readLine());
        }
    }

    @Test
    public void testModifyFirstLine() throws IOException {
        answer.modifyLineInFile(TEST_FILE, 1, "Updated Line 1");
        try (BufferedReader reader = new BufferedReader(new FileReader(TEST_FILE))) {
            assertEquals("Updated Line 1", reader.readLine());
            assertEquals("Line 2", reader.readLine());
            assertEquals("Line 3", reader.readLine());
        }
    }

    @Test
    public void testModifyLastLine() throws IOException {
        answer.modifyLineInFile(TEST_FILE, 3, "Updated Line 3");
        try (BufferedReader reader = new BufferedReader(new FileReader(TEST_FILE))) {
            assertEquals("Line 1", reader.readLine());
            assertEquals("Line 2", reader.readLine());
            assertEquals("Updated Line 3", reader.readLine());
        }
    }

    @Test
    public void testModifyNonExistentLine() {
            assertThrows(IllegalArgumentException.class, () -> {
            answer.modifyLineInFile(TEST_FILE, 4, "Should Fail");
        });
    }

    @Test
    public void testModifyNegativeLineNumber() {
            assertThrows(IllegalArgumentException.class, () -> {
            answer.modifyLineInFile(TEST_FILE, 0, "Should Fail");
        });
    }

}