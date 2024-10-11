package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Answer {

    /**
     * Read a text file, replace words according to a dictionary map, and return the modified text.
     *
     * @param filePath       The path to the text file.
     * @param replacementDict A dictionary where the keys are words to be replaced, and the values are the replacement words.
     * @return The text with the words replaced.
     */
    public static String replaceWordsInFile(String filePath, Map<String, String> replacementDict) {
        StringBuilder result = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                for (Map.Entry<String, String> entry : replacementDict.entrySet()) {
                    line = line.replace(entry.getKey(), entry.getValue());
                }
                result.append(line).append("\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return result.toString().trim(); // Remove trailing newline
    }

    public static void main(String[] args) {
        // Example usage
        Map<String, String> replacements = new HashMap<>();
        replacements.put("hello", "hi");
        replacements.put("world", "earth");

        String filePath = "path/to/your/file.txt";
        String modifiedText = replaceWordsInFile(filePath, replacements);
        System.out.println(modifiedText);
    }
}