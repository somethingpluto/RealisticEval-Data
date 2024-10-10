import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static List<List<Double>> readColumns(String fileName) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.contains("/")) {
                    break; // Stop reading when we find a line with '/'
                }
            }

            List<List<Double>> result = new ArrayList<>();
            while ((line = br.readLine()) != null) {
                String[] numbers = line.split("\\s+");
                List<Double> row = new ArrayList<>();
                for (String num : numbers) {
                    row.add(Double.parseDouble(num));
                }
                result.add(row);
            }

            return result;
        } catch (IOException e) {
            throw new IOException("Error occurred while reading the file", e);
        }
    }
}