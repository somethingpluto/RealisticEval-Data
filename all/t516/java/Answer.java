package org.real.temp;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;
import org.yaml.snakeyaml.reader.ReaderException;

public class Answer {

    /**
     * Reads a YAML file and returns its content as a Java Map or List.
     *
     * @param filePath The path to the YAML file.
     * @return The parsed YAML content as a Java data structure.
     * @throws FileNotFoundException If the specified file does not exist.
     * @throws ReaderException If there is an error parsing the YAML file.
     */
    public Object readYaml(String filePath) throws FileNotFoundException, ReaderException {
        // Check if the file exists
        File file = new File(filePath);
        if (!file.isFile()) {
            throw new FileNotFoundException("The file '" + filePath + "' does not exist.");
        }

        try (InputStream inputStream = new FileInputStream(file)) {
            Yaml yaml = new Yaml(new Constructor(Object.class));
            return yaml.load(inputStream);
        } catch (ReaderException e) {
            throw new ReaderException("Error parsing YAML file: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        Answer answer = new Answer();
        try {
            Object data = answer.readYaml("path/to/your/file.yaml");
            System.out.println(data);
        } catch (FileNotFoundException | ReaderException e) {
            e.printStackTrace();
        }
    }
}