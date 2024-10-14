package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Read a mapping file and return a list of tuples with compiled regex and replacement strings.
     *
     * @param mappingFilePath Path to the file containing regex mappings.
     * @return List of tuples: Each tuple contains a compiled regex object and a corresponding replacement string.
     * @throws IOException If the mapping file does not exist or cannot be read.
     * @throws IllegalArgumentException If any line in the file does not contain exactly one comma.
     */
    public static List<Tuple<Pattern, String>> readMappingFile(String mappingFilePath) throws IOException {
        List<Tuple<Pattern, String>> mappings = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(mappingFilePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (!line.contains(",")) {
                    throw new IllegalArgumentException(
                            "Each line must contain exactly one comma separating the pattern and the replacement.");
                }

                String[] parts = line.split(",", 2);
                String oldPattern = parts[0].trim().replaceAll("^'|'$", "");
                String newWord = parts[1].trim().replaceAll("^'|'$", "");
                mappings.add(new Tuple<>(Pattern.compile(oldPattern), newWord));
            }
        } catch (IOException e) {
            throw new IOException("Unable to find the specified file: " + mappingFilePath, e);
        }

        return mappings;
    }

    // Simple Tuple class implementation for demonstration purposes
    public static class Tuple<T1, T2> {
        private T1 first;
        private T2 second;

        public Tuple(T1 first, T2 second) {
            this.first = first;
            this.second = second;
        }

        public T1 getFirst() {
            return first;
        }

        public T2 getSecond() {
            return second;
        }
    }

    public static void main(String[] args) {
        try {
            List<Tuple<Pattern, String>> mappings = readMappingFile("path/to/mapping/file.txt");
            mappings.forEach(tuple -> System.out.println(tuple.getFirst() + ", " + tuple.getSecond()));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
