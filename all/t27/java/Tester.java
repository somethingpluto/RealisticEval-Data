package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;

import static org.junit.Assert.*;

public class Tester {
    private String testDir;

    @Before
    public void setUp() throws IOException {
        // Set up a test directory and JSON files
        testDir = "test_json";
        Files.createDirectories(Paths.get(testDir));
        createTestFile("array1.json", Arrays.asList(1, 2, 3));
        createTestFile("array2.json", Arrays.asList("a", "b", "c"));
        createTestFile("not_array.json", "{\"key\": \"value\"}");
        createTestFile("empty.json", Arrays.asList());
        createTestFile("non_json.txt", "This is not a JSON file.");
    }

    @After
    public void tearDown() throws IOException {
        // Clean up: Remove created files and directory
        File dir = new File(testDir);
        for (File file : dir.listFiles()) {
            file.delete();
        }
        dir.delete();
    }

    private void createTestFile(String filename, Object content) throws IOException {
        // Helper method to create JSON files
        try (FileWriter writer = new FileWriter(new File(testDir, filename))) {
            if (content instanceof String) {
                writer.write((String) content);
            } else {
                writer.write(new com.google.gson.Gson().toJson(content));
            }
        }
    }

    @Test
    public void testConcatenateValidJsonArrays() {
        // Test with valid JSON arrays
        Object result = ConcatenateJsonArrays.concatenate(testDir);
        assertArrayEquals(new Object[]{1, 2, 3, "a", "b", "c"}, (Object[]) result);
    }

    @Test
    public void testIgnoreNonArrayJson() {
        // Test that non-array JSON files are ignored
        Object result = ConcatenateJsonArrays.concatenate(testDir);
        assertFalse(Arrays.asList((Object[]) result).contains("key"));
    }

    @Test
    public void testIgnoreNonJsonFiles() {
        // Test that non-JSON files are ignored
        Object result = ConcatenateJsonArrays.concatenate(testDir);
        assertFalse(Arrays.asList((Object[]) result).contains("This is not a JSON file."));
    }

    @Test
    public void testHandleEmptyArrays() {
        // Test concatenation includes empty arrays
        Object result = ConcatenateJsonArrays.concatenate(testDir);
        assertFalse(Arrays.asList((Object[]) result).contains(Arrays.asList()));
    }

    @Test
    public void testEmptyDirectory() throws IOException {
        // Test with no JSON files in the directory
        String emptyDir = "empty_test_json";
        Files.createDirectories(Paths.get(emptyDir));
        Object result = ConcatenateJsonArrays.concatenate(emptyDir);
        assertEquals(0, ((Object[]) result).length);
        new File(emptyDir).delete();
    }
}
