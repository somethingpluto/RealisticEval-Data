package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    public List<Object> readDataFromFile(String path) {
        List<Object> dataList = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Trim leading and trailing whitespace
                line = line.trim();

                // Try to parse as an integer
                try {
                    int intValue = Integer.parseInt(line);
                    dataList.add(intValue);
                    continue; // Go to the next line
                } catch (NumberFormatException ignored) {
                    // Not an integer, continue to check for float
                }

                // Try to parse as a floating-point number
                try {
                    float floatValue = Float.parseFloat(line);
                    dataList.add(floatValue);
                    continue; // Go to the next line
                } catch (NumberFormatException ignored) {
                    // Not a float, continue to check for string
                }

                // If it's not an integer or float, it's treated as a string
                dataList.add(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
            throw new IllegalArgumentException("Error reading file: " + e.getMessage());
        }

        return dataList;
    }

    public static void main(String[] args) {
        Answer answer = new Answer();
        List<Object> data = answer.readDataFromFile("path/to/your/file.txt");

        // Print the read data
        for (Object item : data) {
            System.out.println(item + " (" + item.getClass().getSimpleName() + ")");
        }
    }
}
