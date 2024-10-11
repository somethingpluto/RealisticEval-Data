package org.real.temp;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.Map;

public class Answer {

    public static String dataframeToMarkdown(Map<String, List<Object>> df, String mdPath) throws IOException {
        StringBuilder sb = new StringBuilder();

        // Assuming that all columns have the same length
        int columnCount = df.values().iterator().next().size();

        // Adding header row
        for (String columnName : df.keySet()) {
            sb.append("| ").append(columnName).append(" ");
        }
        sb.append("|\n");

        // Adding separator row
        for (int i = 0; i < columnCount; i++) {
            sb.append("| --- ");
        }
        sb.append("|\n");

        // Adding data rows
        for (List<Object> row : df.values()) {
            for (Object cell : row) {
                sb.append("| ").append(cell.toString()).append(" ");
            }
            sb.append("|\n");
        }

        // Writing to file
        try (FileWriter writer = new FileWriter(mdPath)) {
            writer.write(sb.toString());
        }

        return sb.toString();
    }
}