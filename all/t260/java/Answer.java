import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVPrinter;
import org.apache.commons.csv.CSVRecord;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Answer {

    public static void processCSV(String filePath, String outputPath) {
        try (Reader reader = Files.newBufferedReader(Paths.get(filePath));
             CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT.withFirstRecordAsHeader());
             Writer writer = Files.newBufferedWriter(Paths.get(outputPath));
             CSVPrinter csvPrinter = new CSVPrinter(writer, CSVFormat.DEFAULT)) {

            boolean headerPrinted = false;
            for (CSVRecord csvRecord : csvParser) {
                int nullCount = 0;
                for (String value : csvRecord.values()) {
                    if (value == null || value.trim().isEmpty()) {
                        nullCount++;
                    }
                }

                // Skip records with two or more empty columns
                if (nullCount < 2) {
                    if (!headerPrinted) {
                        csvPrinter.printRecord(csvRecord);
                        headerPrinted = true;
                    } else {
                        csvPrinter.printRecord(csvRecord);
                    }
                }
            }
        } catch (IOException e) {
            System.err.println("Error occurred while processing the CSV file: " + e.getMessage());
        }
    }
}