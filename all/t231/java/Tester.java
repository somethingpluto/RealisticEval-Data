package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.BeforeClass;
import org.junit.Test;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Tester {

    private static List<Double> trainLossList = new ArrayList<>();
    private static List<Double> testAcc1List = new ArrayList<>();

    @BeforeClass
    public static void setUp() throws IOException {
        String logFilePath = "path/to/your/logfile.log"; // Replace with actual path
        readLog(logFilePath);
    }

    @Test
    public void testReadLog() {
        assertEquals(10, trainLossList.size()); // Assuming there should be 10 entries
        assertEquals(10, testAcc1List.size()); // Assuming there should be 10 entries

        // Add more specific assertions based on expected values
        assertEquals(0.75, trainLossList.get(0), 0.01);
        assertEquals(88.5, testAcc1List.get(0), 0.01);
    }

    public static void readLog(String logFilePath) throws IOException {
        File file = new File(logFilePath);
        FileReader reader = new FileReader(file);

        StringBuilder sb = new StringBuilder();
        int i;
        while ((i = reader.read()) != -1) {
            sb.append((char) i);
        }
        reader.close();

        JSONArray jsonArray = new JSONArray(sb.toString());
        for (int j = 0; j < jsonArray.length(); j++) {
            JSONObject jsonObject = jsonArray.getJSONObject(j);
            double trainLoss = jsonObject.getDouble("train_loss");
            double testAcc1 = jsonObject.getDouble("test_acc1");

            trainLossList.add(trainLoss);
            testAcc1List.add(testAcc1);
        }
    }
}