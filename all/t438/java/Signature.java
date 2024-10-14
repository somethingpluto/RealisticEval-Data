package org.real.temp;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvValidationException;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Class for reading a CSV file and converting it to a List of Lists representing a DataFrame.
 */
public class Answer {

    /**
     * Reads a CSV file and converts it to a List of Lists representing a DataFrame.
     *
     * @param filePath The path to the CSV file.
     * @return List&lt;List&lt;String&gt;&gt;: List of Lists containing the data from the CSV file.
     */
    public static List<List<String>> readCsvToDataFrame(String filePath) {
        try (CSVReader reader = new CSVReader(new FileReader(filePath))) {
            List<List<String>> dataframe = new ArrayList<>();
            String[] nextLine;
            while ((nextLine = reader.readNext()) != null) {
                List<String> row = new ArrayList<>();
                for (String cell : nextLine) {
                    row.add(cell);
                }
                dataframe.add(row);
            }
            return dataframe;
        } catch (IOException e) {
            System.out.println("Error: The file '" + filePath + "' was not found.");
        } catch (CsvValidationException e) {
            System.out.println("Error: Could not parse the file.");
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
        return null;
    }

    /**
     * Main method to demonstrate reading a CSV file and printing its contents.
     *
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        String filePath = "path/to/your/file.csv";
        List<List<String>> dataframe = readCsvToDataFrame(filePath);
        if (dataframe != null) {
            for (List<String> row : dataframe) {
                System.out.println(row);
            }
        }
    }
}