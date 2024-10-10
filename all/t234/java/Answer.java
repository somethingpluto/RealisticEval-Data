package org.real.temp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static void appendOrSkipRow(String filePath, String[] rowCandidate) {
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath));
             BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {

            List<String> lines = new ArrayList<>();
            String line;

            while ((line = reader.readLine()) != null) {
                String[] currentRow = line.split(",");
                boolean shouldAdd = true;

                for (int i = 0; i < Math.min(currentRow.length, rowCandidate.length); i++) {
                    if (!currentRow[i].equals(rowCandidate[i])) {
                        shouldAdd = false;
                        break;
                    }
                }

                if (shouldAdd) {
                    lines.add(line);
                } else {
                    // Skip adding the row candidate if it matches any existing row
                }
            }

            // Append the new row candidate if no match found
            boolean newRowAdded = false;
            for (String currentRow : lines) {
                String[] currentRowArray = currentRow.split(",");
                boolean shouldAdd = true;

                for (int i = 0; i < Math.min(currentRowArray.length, rowCandidate.length); i++) {
                    if (!currentRowArray[i].equals(rowCandidate[i])) {
                        shouldAdd = false;
                        break;
                    }
                }

                if (shouldAdd) {
                    newRowAdded = true;
                    break;
                }
            }

            if (!newRowAdded) {
                writer.write(String.join(",", rowCandidate));
                writer.newLine();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}