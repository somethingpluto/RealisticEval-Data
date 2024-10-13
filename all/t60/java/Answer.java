package org.real.temp;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvValidationException;

public class Answer {

    /**
     * Finds common column headers across multiple CSV files in a given directory.
     * 
     * @param directoryPath the path to the directory containing CSV files
     * @return a list of common column names
     */
    public static List<String> findCommonColumns(String directoryPath) {
        File directory = new File(directoryPath);
        File[] files = directory.listFiles((dir, name) -> name.toLowerCase().endsWith(".csv"));
        
        if (files == null || files.length == 0) {
            return new ArrayList<>();
        }

        List<Set<String>> columnSets = new ArrayList<>();

        try {
            for (File file : files) {
                CSVReader reader = new CSVReader(new java.io.FileReader(file));
                String[] header = reader.readNext(); // Read the header row
                if (header != null) {
                    columnSets.add(Set.of(header));
                }
                reader.close();
            }
            
            // Use set intersection to find common columns across all CSV files
            if (!columnSets.isEmpty()) {
                Set<String> commonColumns = new ArrayList<>(columnSets.get(0)).stream().collect(Collectors.toSet());
                for (int i = 1; i < columnSets.size(); i++) {
                    commonColumns.retainAll(columnSets.get(i));
                }
                return new ArrayList<>(commonColumns);
            } else {
                return new ArrayList<>();
            }
            
        } catch (Exception e) {
            e.printStackTrace();
            return new ArrayList<>();
        }
    }

    public static void main(String[] args) {
        // Example usage
        List<String> commonCols = findCommonColumns("path/to/directory");
        System.out.println(commonCols);
    }
}