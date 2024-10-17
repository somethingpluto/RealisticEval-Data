package org.real.temp;

import java.io.FileWriter;
import java.io.IOException;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Saves the provided content to a specified file after cleaning up redundant whitespace.
     *
     * @param content The text content to be saved to the file.
     * @param path    The file path where the content will be saved.
     */
    public static void saveContentToFile(String content, String path) {
        // Remove redundant whitespace from the content.
        // Split the content into lines, strip leading/trailing whitespace,
        // and filter out empty lines.
        content = String.join("\n",
            content.lines()
                   .filter(line -> !line.trim().isEmpty())
                   .map(String::trim)
                   .toArray(String[]::new));

        // Replace multiple spaces with a single space.
        content = Pattern.compile("\\s+").matcher(content).replaceAll(" ");

        // Write the cleaned content to the specified file.
        try (FileWriter writer = new FileWriter(path, false)) {
            writer.write(content);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        // Example usage
        String content = "   This is a test.\n\n\nThis is another test.   \n";
        String path = "example.txt";
        saveContentToFile(content, path);
    }
}