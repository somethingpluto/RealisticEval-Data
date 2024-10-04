package org.real.temp;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Finds and replaces text in a specified file.
     *
     * @param filePath      the path to the file
     * @param searchString  the string to search for
     * @param replaceString the string to replace with
     * @throws IOException if an I/O error occurs reading from the file or writing to the file
     */
    public static void findAndReplaceInFile(Path filePath, String searchString, String replaceString) throws IOException {
        // Read all bytes from the file and convert to a String
        String fileContent = new String(Files.readAllBytes(filePath));

        // Replace the search string with the replacement string
        String replacedContent = fileContent.replaceAll(Pattern.quote(searchString), Matcher.quoteReplacement(replaceString));

        // Write the replaced content back to the file
        Files.write(filePath, replacedContent.getBytes());
    }

    // Example main method for testing purposes
    public static void main(String[] args) {
        try {
            Path path = Paths.get("example.txt"); // Specify the file path here
            String searchString = "oldText"; // Text to search for
            String replaceString = "newText"; // Text to replace with

            findAndReplaceInFile(path, searchString, replaceString);
            System.out.println("Replacement done successfully.");
        } catch (IOException e) {
            System.err.println("Error occurred: " + e.getMessage());
        }
    }
}
