package org.real.temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static void main(String[] args) {
        List<List<String>> paddedData = readTSVFromStdin();
        // Example output (for demonstration purposes)
        for (List<String> row : paddedData) {
            System.out.println(row);
        }
    }

    /**
     * Reads TSV data from standard input and pads rows to ensure they have the same length.
     *
     * @return A list of lists containing the padded data.
     */
    public static List<List<String>> readTSVFromStdin() {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        List<List<String>> data = new ArrayList<>();
        String line;

        try {
            while ((line = reader.readLine()) != null) {
                String[] row = line.split("\t");
                data.add(List.of(row));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        int maxColumns = data.isEmpty() ? 0 : data.stream()
                .mapToInt(row -> row.size())
                .max()
                .orElse(0);

        List<List<String>> paddedData = new ArrayList<>();
        for (List<String> row : data) {
            List<String> paddedRow = new ArrayList<>(row);
            paddedRow.addAll(List.of(new String[maxColumns - row.size()]));
            paddedData.add(paddedRow);
        }

        return paddedData;
    }
}