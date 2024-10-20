import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.JsonSyntaxException;

public class Answer {

    public static void main(String[] args) {
        String logFilePath = "path/to/your/log/file.log";
        List<Double> trainLossList;
        List<Double> testAcc1List;

        try {
            trainLossList = new ArrayList<>();
            testAcc1List = new ArrayList<>();
            readLog(logFilePath, trainLossList, testAcc1List);
        } catch (IOException e) {
            System.out.println("An error occurred while reading the log file.");
            e.printStackTrace();
        }

        System.out.println("Train Loss List: " + trainLossList);
        System.out.println("Test Acc1 List: " + testAcc1List);
    }

    public static void readLog(String logFilePath, List<Double> trainLossList, List<Double> testAcc1List) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(logFilePath))) {
            String line;
            Gson gson = new Gson();

            while ((line = reader.readLine()) != null) {
                try {
                    LogEntry entry = gson.fromJson(line, LogEntry.class);
                    if (entry.trainLoss != null) {
                        trainLossList.add(entry.trainLoss);
                    }
                    if (entry.testAcc1 != null) {
                        testAcc1List.add(entry.testAcc1);
                    }
                } catch (JsonSyntaxException e) {
                    System.out.println("Error: The file " + logFilePath + " contains invalid JSON.");
                    return;
                }
            }
        } catch (IOException e) {
            System.out.println("Error: The file " + logFilePath + " does not exist.");
            throw e;
        }
    }

    // A simple POJO class to represent the log entries
    private static class LogEntry {
        Double trainLoss;
        Double testAcc1;
    }
}