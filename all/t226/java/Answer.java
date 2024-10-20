package org.real.temp;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.LinkedHashMap;
import java.util.Map;

public class Answer {

    public static void tsvToJSONL(String tsvFilePath, String jsonlFilePath) {
        try (Reader reader = Files.newBufferedReader(Paths.get(tsvFilePath));
             CSVParser csvParser = new CSVParser(reader, CSVFormat.TSV);
             Writer writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(jsonlFilePath), "UTF-8"))) {

            // Parse the TSV file
            Iterable<CSVRecord> records = csvParser.getRecords();
            ObjectMapper objectMapper = new ObjectMapper();

            for (CSVRecord record : records) {
                // Convert each record to a Map
                Map<String, String> rowMap = new LinkedHashMap<>();
                for (String header : csvParser.getHeaderNames()) {
                    rowMap.put(header, record.get(header));
                }

                // Convert the Map to JSON string
                String jsonLine = objectMapper.writeValueAsString(rowMap);

                // Write the JSON line to the JSONL file
                writer.write(jsonLine + "\n");
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        // Example usage
        tsvToJSONL("path/to/input.tsv", "path/to/output.jsonl");
    }
}