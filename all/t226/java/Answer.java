package org.real.temp;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static void tsvToJsonl(String tsvFile, String jsonlFile) {
        try (Reader reader = new FileReader(tsvFile);
             BufferedWriter writer = new BufferedWriter(new FileWriter(jsonlFile));
             CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT.withHeader().withIgnoreHeaderCase().trim())) {

            List<String> headers = csvParser.getHeaderMap().keySet();
            Gson gson = new GsonBuilder().setPrettyPrinting().create();

            for (CSVRecord record : csvParser) {
                StringBuilder jsonLine = new StringBuilder();
                jsonLine.append("{");
                for (String header : headers) {
                    jsonLine.append("\"").append(header).append("\": \"").append(record.get(header)).append("\", ");
                }
                // Remove the trailing comma and space
                jsonLine.deleteCharAt(jsonLine.length() - 2);
                jsonLine.append("}\n");
                writer.write(jsonLine.toString());
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        tsvToJsonl("path/to/your/input.tsv", "path/to/your/output.jsonl");
    }
}