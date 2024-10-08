package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Answer{
/**
 * Reads a file from the specified path, processes each line to remove inline comments,
 * removes line breaks, and returns a list of the processed line contents.
 *
 * @param path The path to the file to be read.
 * @return A list of strings, each representing a processed line from the file.
 * @throws IllegalArgumentException if an I/O error occurs while reading the file.
 */
public List<String> readFileAndProcessLines(String path) {
    List<String> processedLines = new ArrayList<>();

    try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
        String line;

        while ((line = reader.readLine()) != null) {
            // Remove inline comments
            line = line.split("#")[0].trim();
            // Only add non-empty lines to the list
            if (!line.isEmpty()) {
                processedLines.add(line);
            }
        }
    } catch (IOException e) {
        e.printStackTrace();
        throw new IllegalArgumentException("Error reading file: " + e.getMessage());
    }

    return processedLines;
}
}
