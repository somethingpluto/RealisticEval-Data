import java.io.*;
import java.util.*;

public class Answer {
    public static void extractLogEntries(String logFilePath) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(logFilePath));
        String line;
        Map<String, BufferedWriter> writers = new HashMap<>();

        while ((line = reader.readLine()) != null) {
            if (line.contains("WARNING")) {
                getWriter(writers, "warnings.log").write(line + "\n");
            } else if (line.contains("ERROR")) {
                getWriter(writers, "errors.log").write(line + "\n");
            } else if (line.contains("CRITICAL")) {
                getWriter(writers, "criticals.log").write(line + "\n");
            } else if (line.contains("ALERT")) {
                getWriter(writers, "alerts.log").write(line + "\n");
            }
        }

        for (BufferedWriter writer : writers.values()) {
            writer.close();
        }

        reader.close();
    }

    private static BufferedWriter getWriter(Map<String, BufferedWriter> writers, String fileName) throws IOException {
        BufferedWriter writer = writers.get(fileName);
        if (writer == null) {
            writer = new BufferedWriter(new FileWriter(fileName, true));
            writers.put(fileName, writer);
        }
        return writer;
    }
}