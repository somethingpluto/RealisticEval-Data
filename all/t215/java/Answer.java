package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Map;

public class Answer {

    /**
     * Reads a text file, replaces words according to a map, and returns the modified text.
     *
     * @param filePath The path to the text file.
     * @param replacementMap A map where the keys are words to be replaced, and the values are the replacement words.
     * @return The text with the words replaced or an error message if an exception occurs.
     */
    public static String replaceWordsInFile(String filePath, Map<String, String> replacementMap) {
        StringBuilder text = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                text.append(line).append("\n");
            }

            // Replace words according to the replacement map
            for (Map.Entry<String, String> entry : replacementMap.entrySet()) {
                text = new StringBuilder(text.toString().replace(entry.getKey(), entry.getValue()));
            }

            return text.toString();

        } catch (IOException e) {
            if (e instanceof java.io.FileNotFoundException) {
                return "Error: The file was not found.";
            }
            return "Error: " + e.getMessage();
        } catch (Exception e) {
            return "Error: " + e.getMessage();
        }
    }

    // Example usage
    public static void main(String[] args) {
        Map<String, String> replacementMap = Map.of("oldWord", "newWord");
        String result = replaceWordsInFile("path/to/your/file.txt", replacementMap);
        System.out.println(result);
    }
}