package org.real.temp;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVPrinter;
import org.apache.commons.csv.CSVRecord;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Processes a CSV file and removes rows with two or more empty columns.
     *
     * @param filePath The path to the input CSV file.
     * @param outputPath The path where the processed CSV file will be saved.
     */
    public static void processCsv(String filePath, String outputPath) {
        try (Reader reader = new FileReader(filePath);
             CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT.withFirstRecordAsHeader());
             Writer writer = new FileWriter(outputPath);
             CSVPrinter csvPrinter = new CSVPrinter(writer, CSVFormat.DEFAULT)) {

            List<CSVRecord> records = new ArrayList<>();
            for (CSVRecord record : csvParser) {
                int emptyCount = 0;
                for (String value : record) {
                    if (value == null || value.trim().isEmpty()) {
                        emptyCount++;
                    }
                }

                // Filter the records to keep only those with less than 2 empty columns
                if (emptyCount < 2) {
                    records.add(record);
                }
            }

            // Write the filtered records to the output CSV file
            for (CSVRecord record : records) {
                csvPrinter.printRecord(record);
            }

        } catch (IOException e) {
            System.err.println("Error processing the CSV file: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        String filePath = "path/to/input.csv";
        String outputPath = "path/to/output.csv";
        processCsv(filePath, outputPath);
    }
}