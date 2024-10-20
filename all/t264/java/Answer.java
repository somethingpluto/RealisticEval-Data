package org.real.temp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Answer {

    private static final Map<String, String> outputFiles = new HashMap<>();
    private static final Map<String, ArrayList<String>> logs = new HashMap<>();

    static {
        outputFiles.put("WARNING", "warning_logs.txt");
        outputFiles.put("ERROR", "error_logs.txt");
        outputFiles.put("CRITICAL", "critical_logs.txt");
        outputFiles.put("ALERT", "alert_logs.txt");

        logs.put("WARNING", new ArrayList<>());
        logs.put("ERROR", new ArrayList<>());
        logs.put("CRITICAL", new ArrayList<>());
        logs.put("ALERT", new ArrayList<>());
    }

    public static void extractLogEntries(String logFilePath) throws IOException {
        if (!Files.exists(Paths.get(logFilePath))) {
            throw new IOException("No log file found at the specified path: " + logFilePath);
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(logFilePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                for (String level : logs.keySet()) {
                    if (line.contains(level)) {
                        logs.get(level).add(line);
                        break;
                    }
                }
            }
        }

        for (Map.Entry<String, ArrayList<String>> entry : logs.entrySet()) {
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFiles.get(entry.getKey())))) {
                for (String entryLine : entry.getValue()) {
                    writer.write(entryLine);
                    writer.newLine();
                }
                System.out.println("Saved " + entry.getValue().size() + " '" + entry.getKey() + "' entries to " + outputFiles.get(entry.getKey()) + ".");
            }
        }
    }

    public static void main(String[] args) {
        try {
            extractLogEntries("path/to/your/logfile.log");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}