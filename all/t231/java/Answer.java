package org.real.temp;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Answer {

    public static Tuple<List<Double>, List<Double>> readLog(String logFilePath) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        File file = new File(logFilePath);

        // Assuming each line in the file represents a separate JSON object
        List<String> lines = Files.readAllLines(file.toPath());

        List<Double> trainLossList = new ArrayList<>();
        List<Double> testAcc1List = new ArrayList<>();

        for (String line : lines) {
            Map<String, Object> jsonMap = mapper.readValue(line, Map.class);

            if (jsonMap.containsKey("test_acc1") && jsonMap.containsKey("train_loss")) {
                double testAcc1 = (double) jsonMap.get("test_acc1");
                double trainLoss = (double) jsonMap.get("train_loss");

                testAcc1List.add(testAcc1);
                trainLossList.add(trainLoss);
            }
        }

        return new Tuple<>(trainLossList, testAcc1List);
    }

    // Helper class to represent a tuple
    public static class Tuple<X, Y> {
        private X first;
        private Y second;

        public Tuple(X first, Y second) {
            this.first = first;
            this.second = second;
        }

        public X getFirst() { return first; }
        public Y getSecond() { return second; }
    }
}