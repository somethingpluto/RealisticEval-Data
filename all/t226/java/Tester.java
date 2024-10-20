package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import static org.real.temp.Answer.*;
import static org.junit.Assert.assertEquals;

/**
 * Tests for the TSV to JSONL conversion.
 */
public class Tester {

    private Path tempDir;

    /**
     * Sets up a temporary directory for testing.
     */
    @Before
    public void setUp() throws IOException {
        // Create a temporary directory
        tempDir = Files.createTempDirectory("testDir");
    }

    /**
     * Cleans up the temporary directory after each test.
     */
    @After
    public void tearDown() throws IOException {
        // Delete the temporary directory and its contents
        Files.walk(tempDir)
                .sorted((path1, path2) -> path2.compareTo(path1)) // Delete files before directories
                .forEach(path -> {
                    try {
                        Files.delete(path);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                });
    }

    /**
     * Tests the conversion of a standard TSV file to JSONL.
     */
    @Test
    public void testStandardTSV() throws IOException {
        String tsvContent = "Name\tAge\tCountry\nAlice\t30\tUSA\nBob\t25\tCanada\n";
        Path tsvFile = tempDir.resolve("test_standard.tsv");
        Path jsonlFile = tempDir.resolve("test_standard.jsonl");

        try (Writer writer = new BufferedWriter(new OutputStreamWriter(Files.newOutputStream(tsvFile), "UTF-8"))) {
            writer.write(tsvContent);
        }

        tsvToJSONL(tsvFile.toString(), jsonlFile.toString());

        List<String> lines = Files.readAllLines(jsonlFile);

        List<String> expectedLines = List.of(
                "{\"Name\":\"Alice\",\"Age\":30,\"Country\":\"USA\"}\n",
                "{\"Name\":\"Bob\",\"Age\":25,\"Country\":\"Canada\"}\n"
        );

        assertEquals(expectedLines, lines);
    }

    /**
     * Tests the conversion of a single-row TSV file to JSONL.
     */
    @Test
    public void testSingleRowTSV() throws IOException {
        String tsvContent = "Name\tAge\tCountry\nAlice\t30\tUSA\n";
        Path tsvFile = tempDir.resolve("test_single_row.tsv");
        Path jsonlFile = tempDir.resolve("test_single_row.jsonl");

        try (Writer writer = new BufferedWriter(new OutputStreamWriter(Files.newOutputStream(tsvFile), "UTF-8"))) {
            writer.write(tsvContent);
        }

        tsvToJSONL(tsvFile.toString(), jsonlFile.toString());

        List<String> lines = Files.readAllLines(jsonlFile);

        List<String> expectedLines = List.of(
                "{\"Name\":\"Alice\",\"Age\":30,\"Country\":\"USA\"}\n"
        );

        assertEquals(expectedLines, lines);
    }

    /**
     * Tests the conversion of a TSV file with numeric and boolean values to JSONL.
     */
    @Test
    public void testNumericAndBooleanValues() throws IOException {
        String tsvContent = "Name\tAge\tIs_Student\nAlice\t30\tTrue\nBob\t25\tFalse\n";
        Path tsvFile = tempDir.resolve("test_numeric_boolean.tsv");
        Path jsonlFile = tempDir.resolve("test_numeric_boolean.jsonl");

        try (Writer writer = new BufferedWriter(new OutputStreamWriter(Files.newOutputStream(tsvFile), "UTF-8"))) {
            writer.write(tsvContent);
        }

        tsvToJSONL(tsvFile.toString(), jsonlFile.toString());

        List<String> lines = Files.readAllLines(jsonlFile);

        List<String> expectedLines = List.of(
                "{\"Name\":\"Alice\",\"Age\":30,\"Is_Student\":true}\n",
                "{\"Name\":\"Bob\",\"Age\":25,\"Is_Student\":false}\n"
        );

        assertEquals(expectedLines, lines);
    }
}
