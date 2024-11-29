package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertThrows;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Tester {

    private static final String LOG_FILE_PATH = "test_log.log";
    private static final String[] LOG_CONTENTS = {
        "INFO: This is an informational message.\n",
        "WARNING: This is a warning message.\n",
        "ERROR: This is an error message.\n",
        "CRITICAL: This is a critical message.\n",
        "ALERT: This is an alert message.\n"
    };

    @Before
    public void setUp() throws IOException {
        File logFile = new File(LOG_FILE_PATH);
        try (FileWriter writer = new FileWriter(logFile)) {
            for (String line : LOG_CONTENTS) {
                writer.write(line);
            }
        }
    }

    @Test
    public void testNoLogsOfCertainLevels() throws IOException {
        // Setup a log file with only INFO messages
        File logFile = new File(LOG_FILE_PATH);
        try (FileWriter writer = new FileWriter(logFile)) {
            writer.write("INFO: This is another informational message.\n");
        }

        extractLogEntries(LOG_FILE_PATH);

        for (String level : new String[]{"WARNING", "ERROR", "CRITICAL", "ALERT"}) {
            File outputFile = new File(level.toLowerCase() + "_logs.txt");
            assertEquals("", Files.readString(outputFile.toPath()));
        }
    }

    @Test
    public void testFileNotFound() {
        assertThrows(IOException.class, () -> extractLogEntries("nonexistent.log"));
    }

    @Test
    public void testEmptyLogFile() throws IOException {
        // Setup an empty log file
        File logFile = new File(LOG_FILE_PATH);
        try (FileWriter writer = new FileWriter(logFile)) {
            writer.write("");
        }

        extractLogEntries(LOG_FILE_PATH);

        for (String level : new String[]{"WARNING", "ERROR", "CRITICAL", "ALERT"}) {
            File outputFile = new File(level.toLowerCase() + "_logs.txt");
            assertEquals("", Files.readString(outputFile.toPath()));
        }
    }

    @Test
    public void testMixedContentLogFile() throws IOException {
        // Setup a log file with mixed content
        File logFile = new File(LOG_FILE_PATH);
        try (FileWriter writer = new FileWriter(logFile)) {
            writer.write("INFO: Some info.\n");
            writer.write("WARNING: Watch out!\n");
            writer.write("DEBUG: Debugging.\n");
            writer.write("ERROR: Oops!\n");
            writer.write("CRITICAL: Failed badly.\n");
            writer.write("ALERT: High alert!\n");
            writer.write("INFO: More info.\n");
        }

        extractLogEntries(LOG_FILE_PATH);

        for (String level : new String[]{"WARNING", "ERROR", "CRITICAL", "ALERT"}) {
            File outputFile = new File(level.toLowerCase() + "_logs.txt");
            String content = Files.readString(outputFile.toPath()).trim();
            assertTrue(content.contains(level));
        }
    }

    // Method to be tested
    public static void extractLogEntries(String logFilePath) throws IOException {
        if (!Files.exists(Paths.get(logFilePath))) {
            throw new IOException("No log file found at the specified path: " + logFilePath);
        }

        Map<String, String> outputFiles = new HashMap<>();
        outputFiles.put("WARNING", "warning_logs.txt");
        outputFiles.put("ERROR", "error_logs.txt");
        outputFiles.put("CRITICAL", "critical_logs.txt");
        outputFiles.put("ALERT", "alert_logs.txt");

        Map<String, ArrayList<String>> logs = new HashMap<>();
        logs.put("WARNING", new ArrayList<>());
        logs.put("ERROR", new ArrayList<>());
        logs.put("CRITICAL", new ArrayList<>());
        logs.put("ALERT", new ArrayList<>());

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
}