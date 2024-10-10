package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Answer {

    public static String csvToSqlInsert(String csvFilePath) {
        StringBuilder sb = new StringBuilder();

        try (BufferedReader br = new BufferedReader(new FileReader(csvFilePath))) {
            String line;

            while ((line = br.readLine()) != null) {
                // Assuming that the CSV has headers and each row represents a record
                String[] values = line.split(",");

                if (sb.length() > 0)
                    sb.append("\n");

                // Replace "table_name" with your actual table name without suffix
                sb.append("INSERT INTO table_name VALUES (");

                for (int i = 0; i < values.length; ++i) {
                    if (i > 0)
                        sb.append(", ");

                    // If the value contains commas or single quotes, enclose it in single quotes
                    if (values[i].contains(",") || values[i].contains("'"))
                        sb.append("'").append(values[i]).append("'");
                    else
                        sb.append(values[i]);
                }

                sb.append(");");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return sb.toString();
    }
}