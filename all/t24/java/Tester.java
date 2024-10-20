package org.real.temp;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
import com.fasterxml.jackson.core.JsonProcessingException;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.Rule;
import org.junit.rules.TemporaryFolder;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

/**
 * Tests for converting YAML files to JSON files.
 */
public class Tester {

    private static final String SIMPLE_YAML = "simple.yaml";
    private static final String NESTED_YAML = "nested.yaml";
    private static final String EMPTY_YAML = "empty.yaml";
    private static final String LIST_YAML = "list.yaml";
    private static final String INVALID_YAML = "invalid.yaml";

    @Rule
    public TemporaryFolder tempFolder = new TemporaryFolder();

    private Path tempDir;

    @Before
    public void setUp() throws IOException {
        this.tempDir = tempFolder.newFolder().toPath();

        // Create temporary YAML files for testing
        writeYamlFile(tempDir.resolve(SIMPLE_YAML), "name: John Doe\nage: 30\n");
        writeYamlFile(tempDir.resolve(NESTED_YAML), "person:\n  name: Jane Doe\n  age: 25\n  address:\n    city: New York\n    zip: 10001\n");
        writeYamlFile(tempDir.resolve(EMPTY_YAML), "");
        writeYamlFile(tempDir.resolve(LIST_YAML), "- item1\n- item2\n- item3\n");
        writeYamlFile(tempDir.resolve(INVALID_YAML), "{ invalid: YAML: structure }\n");
    }

    @After
    public void tearDown() {
        // No explicit cleanup required with TemporaryFolder
    }

    @Test
    public void testSimpleYamlConversion() throws IOException {
        convertYamlToJson(tempDir.resolve(SIMPLE_YAML).toString(), "output.json");
        assertEquals("{\"name\":\"John Doe\",\"age\":30}", readFileContent(tempDir.resolve("output.json")));
    }

    @Test
    public void testNestedYamlConversion() throws IOException {
        convertYamlToJson(tempDir.resolve(NESTED_YAML).toString(), "output.json");
        assertEquals("{\"person\":{\"name\":\"Jane Doe\",\"age\":25,\"address\":{\"city\":\"New York\",\"zip\":10001}}}", readFileContent(tempDir.resolve("output.json")));
    }

    @Test
    public void testEmptyYamlConversion() throws IOException {
        convertYamlToJson(tempDir.resolve(EMPTY_YAML).toString(), "output.json");
        assertEquals("", readFileContent(tempDir.resolve("output.json")));  // YAML.safe_load() returns null, but JSON dump of null is ""
    }

    @Test
    public void testListYamlConversion() throws IOException {
        convertYamlToJson(tempDir.resolve(LIST_YAML).toString(), "output.json");
        assertEquals("[\"item1\",\"item2\",\"item3\"]", readFileContent(tempDir.resolve("output.json")));
    }

    @Test
    public void testInvalidYamlConversion() {
        assertThrows(Exception.class, () -> convertYamlToJson(tempDir.resolve(INVALID_YAML).toString(), "output.json"));
    }

    private void writeYamlFile(Path filePath, String content) throws IOException {
        try (FileWriter writer = new FileWriter(filePath.toFile())) {
            writer.write(content);
        }
    }

    private String readFileContent(Path filePath) throws IOException {
        return new String(java.nio.file.Files.readAllBytes(filePath));
    }
}
