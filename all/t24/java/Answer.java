package org.real.temp;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
import com.fasterxml.jackson.core.JsonProcessingException;

import java.io.File;
import java.io.IOException;

/**
 * Converts a YAML file to a JSON file.
 */
public class Answer {

    /**
     * Convert a YAML file to a JSON file.
     *
     * @param yamlFilePath  Path to the input YAML file.
     * @param jsonFilePath  Path to the output JSON file.
     */
    public static void convertYamlToJson(String yamlFilePath, String jsonFilePath) {
        ObjectMapper yamlReader = new ObjectMapper(new YAMLFactory());
        ObjectMapper jsonWriter = new ObjectMapper();

        try {
            // Read the YAML file
            Object data = yamlReader.readValue(new File(yamlFilePath), Object.class);

            // Write the data to a JSON file
            jsonWriter.writerWithDefaultPrettyPrinter().writeValue(new File(jsonFilePath), data);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        // Example usage
        convertYamlToJson("path/to/input.yaml", "path/to/output.json");
    }
}