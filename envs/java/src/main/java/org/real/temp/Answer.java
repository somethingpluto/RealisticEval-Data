package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Reads a CSV file and parses each line into a list of strings.
     *
     * @param filePath The path to the CSV file.
     * @return A list of string arrays, where each array represents a line from the CSV.
     * @throws IOException If there is an error reading the file.
     */
    public List<List<String>> readCsv(String filePath) throws IOException {
        List<List<String>> result = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                List<String> lineList = new ArrayList<>();
                for (String value : values) {
                    lineList.add(value.trim());
                }
                result.add(lineList);
            }
        }
        return result;
    }
}