package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.json.JSONObject;
import static org.real.temp.Answer.*;
public class Tester {

    private static final String VALID_JSONL_FILE = "test_valid.jsonl";
    private static final String INVALID_JSONL_FILE = "test_invalid.jsonl";
    private static final String NON_EXISTENT_FILE = "non_existent.jsonl";
    private static final String EMPTY_JSONL_FILE = "test_empty.jsonl";

    @Before
    public void setUp() throws IOException {
        // Valid JSON Lines content
        try (FileWriter writer = new FileWriter(VALID_JSONL_FILE)) {
            writer.write("{\"name\": \"Alice\", \"age\": 30}\n");
            writer.write("{\"name\": \"Bob\", \"age\": 25}\n");
            writer.write("{\"name\": \"Charlie\", \"age\": 35}\n");
        }

        // Invalid JSON Lines content
        try (FileWriter writer = new FileWriter(INVALID_JSONL_FILE)) {
            writer.write("{\"name\": \"Alice\", \"age\": 30}\n");
            writer.write("{\"name\": \"Bob\", \"age\": \"twenty-five}\n");  // Missing closing quote
        }
    }

    @After
    public void tearDown() {
        // Remove the temporary JSON Lines files after testing
        new File(VALID_JSONL_FILE).delete();
        new File(INVALID_JSONL_FILE).delete();
        new File(EMPTY_JSONL_FILE).delete();
    }

    @Test
    public void testReadValidJsonl() throws IOException {
        // Test reading a valid JSON Lines file
        List<JSONObject> expectedData = new ArrayList<>();
        expectedData.add(new JSONObject().put("name", "Alice").put("age", 30));
        expectedData.add(new JSONObject().put("name", "Bob").put("age", 25));
        expectedData.add(new JSONObject().put("name", "Charlie").put("age", 35));

        List<JSONObject> result = readJsonl(VALID_JSONL_FILE);
        assertEquals(expectedData, result);
    }

    @Test(expected = IOException.class)
    public void testFileNotFound() throws IOException {
        // Test for FileNotFoundException when the file does not exist
        readJsonl(NON_EXISTENT_FILE);
    }

    @Test
    public void testEmptyJsonlFile() throws IOException {
        // Test reading an empty JSON Lines file
        try (FileWriter writer = new FileWriter(EMPTY_JSONL_FILE)) {
            writer.write("");  // Create an empty JSON Lines file
        }

        List<JSONObject> result = readJsonl(EMPTY_JSONL_FILE);
        assertEquals(new ArrayList<>(), result);

        // Cleanup after the test
        new File(EMPTY_JSONL_FILE).delete();
    }
}