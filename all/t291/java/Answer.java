package org.real.temp;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Answer {

    /**
     * Appends the specified string to the beginning of each line of the file.
     *
     * @param filePath the path to the file whose lines will be modified
     * @param prefix   the string to append to the beginning of each line
     */
    public static void prependToEachLine(String filePath, String prefix) {
        String tempFilePath = filePath + ".tmp";

        try {
            // Read all lines from the original file
            List<String> lines = Files.readAllLines(Paths.get(filePath));

            // Write the modified lines to a temporary file
            try (FileWriter tempFileWriter = new FileWriter(tempFilePath)) {
                for (String line : lines) {
                    tempFileWriter.write(prefix + line);
                    tempFileWriter.write(System.lineSeparator());
                }
            }

            // Replace the original file with the temporary file
            File originalFile = new File(filePath);
            File tempFile = new File(tempFilePath);
            if (!tempFile.renameTo(originalFile)) {
                throw new IOException("Failed to rename temporary file to original file.");
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        // Example usage
        prependToEachLine("example.txt", "Prefix: ");
    }
}