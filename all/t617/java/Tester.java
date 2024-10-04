package org.real.temp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

public class Tester {

    private static final String VALID_JSON_FILE = "valid.json";
    private static final String INVALID_JSON_FILE = "invalid.json";
    private static final String EMPTY_JSON_FILE = "empty.json";
    private static final String NESTED_JSON_FILE = "nested.json";

    @BeforeEach
    public void setUp() throws IOException {
        // Create a valid JSON file
        createJsonFile(VALID_JSON_FILE, "{\"name\": \"John\", \"age\": 30}");

        // Create an invalid JSON file
        createJsonFile(INVALID_JSON_FILE, "{\"name\": \"John\", \"age\": 30,}");

        // Create an empty JSON file
        createJsonFile(EMPTY_JSON_FILE, "");

        // Create a nested JSON file
        createJsonFile(NESTED_JSON_FILE, "{\"user\": {\"name\": \"Alice\", \"age\": 25}, \"active\": true}");
    }

    private void createJsonFile(String fileName, String content) throws IOException {
        try (FileWriter fileWriter = new FileWriter(fileName)) {
            fileWriter.write(content);
        }
    }

    @Test
    public void testParseValidJson() {
        Map<String, Object> result = Answer.parseJsonFile(VALID_JSON_FILE);
        assertEquals("John", result.get("name"));
        assertEquals(30, result.get("age"));
    }

    @Test
    public void testParseInvalidJson() {
        Map<String, Object> result = Answer.parseJsonFile(INVALID_JSON_FILE);
        assertTrue(result.isEmpty(), "Expected empty result for invalid JSON");
    }

    @Test
    public void testParseEmptyJson() {
        Map<String, Object> result = Answer.parseJsonFile(EMPTY_JSON_FILE);
        assertTrue(result.isEmpty(), "Expected empty result for empty JSON file");
    }

    @Test
    public void testParseNestedJson() {
        Map<String, Object> result = Answer.parseJsonFile(NESTED_JSON_FILE);
        Map<String, Object> user = (Map<String, Object>) result.get("user");
        assertEquals("Alice", user.get("name"));
        assertEquals(25, user.get("age"));
        assertTrue((Boolean) result.get("active"));
    }

    @Test
    public void testParseNonExistentJsonFile() {
        Map<String, Object> result = Answer.parseJsonFile("non_existent_file.json");
        assertTrue(result.isEmpty(), "Expected empty result for non-existent file");
    }

    @Test
    public void testParseJsonWithSpecialCharacters() throws IOException {
        String specialCharJson = "{\"greeting\": \"Hello, \\\"World\\\"!\"}";
        createJsonFile("special_char.json", specialCharJson);
        Map<String, Object> result = Answer.parseJsonFile("special_char.json");
        assertEquals("Hello, \"World\"!", result.get("greeting"));
    }
}
