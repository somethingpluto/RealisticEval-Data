package org.real.temp;

import org.junit.Before;
import org.junit.After;
import org.junit.Test;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    private Path tempInputFile;
    private Path tempOutputFile;
    private Path tempDir;

    @Before
    public void setUp() throws IOException {
        // Create a temporary directory manually in JUnit 4
        tempDir = Files.createTempDirectory("testDir");
        tempInputFile = tempDir.resolve("input.txt");
        tempOutputFile = tempDir.resolve("output.txt");
    }

    @After
    public void tearDown() {
        try {
            // Clean up the temporary files after tests
            Files.deleteIfExists(tempInputFile);
            Files.deleteIfExists(tempOutputFile);
            Files.deleteIfExists(tempDir);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Test
    public void testBasicText() throws IOException {
        // Test with basic text
        String inputText = "This is line one.\nThis is line two.\nThis is line three.";
        String expectedOutput = "This is line one. This is line two. This is line three.";

        try (FileWriter writer = new FileWriter(tempInputFile.toFile())) {
            writer.write(inputText);
        }

        formatText(tempInputFile.toString(), tempOutputFile.toString());

        String outputText = new String(Files.readAllBytes(tempOutputFile)).trim();

        assertEquals(expectedOutput, outputText);
    }

    @Test
    public void testSingleLine() throws IOException {
        // Test with a single line
        String inputText = "This is a single line.";
        String expectedOutput = "This is a single line.";

        try (FileWriter writer = new FileWriter(tempInputFile.toFile())) {
            writer.write(inputText);
        }

        formatText(tempInputFile.toString(), tempOutputFile.toString());

        String outputText = new String(Files.readAllBytes(tempOutputFile)).trim();

        assertEquals(expectedOutput, outputText);
    }

    @Test
    public void testEmptyFile() throws IOException {
        // Test with an empty file
        String inputText = "";
        String expectedOutput = "";

        try (FileWriter writer = new FileWriter(tempInputFile.toFile())) {
            writer.write(inputText);
        }

        formatText(tempInputFile.toString(), tempOutputFile.toString());

        String outputText = new String(Files.readAllBytes(tempOutputFile)).trim();

        assertEquals(expectedOutput, outputText);
    }

    @Test
    public void testFileWithNoNewlines() throws IOException {
        // Test with text that has no newlines
        String inputText = "This is a continuous line without breaks.";
        String expectedOutput = "This is a continuous line without breaks.";

        try (FileWriter writer = new FileWriter(tempInputFile.toFile())) {
            writer.write(inputText);
        }

        formatText(tempInputFile.toString(), tempOutputFile.toString());

        String outputText = new String(Files.readAllBytes(tempOutputFile)).trim();

        assertEquals(expectedOutput, outputText);
    }
}
