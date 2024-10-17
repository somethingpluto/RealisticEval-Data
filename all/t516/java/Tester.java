package org.real.temp;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;
import org.yaml.snakeyaml.reader.ReaderException;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

/**
 * Test class for reading YAML files.
 */
public class Tester {

    private String validYamlFile = "test_valid.yaml";
    private String invalidYamlFile = "test_invalid.yaml";
    private String nonExistentFile = "non_existent.yaml";
    private String emptyYamlFile = "test_empty.yaml";

    @BeforeEach
    public void setUp() throws IOException {
        // Valid YAML content
        try (FileWriter writer = new FileWriter(validYamlFile)) {
            writer.write("name: Example\nversion: 1.0\ndependencies:\n  - package1\n  - package2\n");
        }

        // Invalid YAML content
        try (FileWriter writer = new FileWriter(invalidYamlFile)) {
            writer.write("name: Example\nversion: 1.0\ndependencies:\n  - package1\n  - package2\ninvalid_yaml: \n - ");
        }
    }

    @AfterEach
    public void tearDown() {
        // Remove the temporary YAML files after testing
        new File(validYamlFile).delete();
        new File(invalidYamlFile).delete();
        new File(emptyYamlFile).delete();
    }

    @Test
    public void testReadValidYaml() throws IOException {
        // Test reading a valid YAML file
        Map<String, Object> expectedData = Map.of(
            "name", "Example",
            "version", 1.0,
            "dependencies", new String[]{"package1", "package2"}
        );

        Object result = readYaml(validYamlFile);
        assertEquals(expectedData, result);
    }

    @Test
    public void testFileNotFound() {
        // Test for FileNotFoundError when the file does not exist
        assertThrows(FileNotFoundException.class, () -> readYaml(nonExistentFile));
    }

    @Test
    public void testEmptyYamlFile() throws IOException {
        // Test reading an empty YAML file
        try (FileWriter writer = new FileWriter(emptyYamlFile)) {
            writer.write("");  // Create an empty YAML file
        }

        Object result = readYaml(emptyYamlFile);
        assertEquals(null, result);  // Expecting null for empty file
    }

    /**
     * Reads a YAML file and returns its content as a Java data structure.
     *
     * @param filePath The path to the YAML file.
     * @return The parsed YAML content as a Java data structure.
     * @throws FileNotFoundException If the specified file does not exist.
     * @throws ReaderException If there is an error parsing the YAML file.
     */
    private Object readYaml(String filePath) throws FileNotFoundException, ReaderException {
        File file = new File(filePath);
        if (!file.isFile()) {
            throw new FileNotFoundException("The file '" + filePath + "' does not exist.");
        }

        try (FileInputStream inputStream = new FileInputStream(file)) {
            Yaml yaml = new Yaml(new Constructor(Object.class));
            return yaml.load(inputStream);
        } catch (ReaderException e) {
            throw new ReaderException("Error parsing YAML file: " + e.getMessage());
        }
    }
}