package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.ArrayList;
import java.util.List;

public class Tester {

    /**
     * Test case for no inconsistencies in the records.
     */
    @Test
    public void testNoInconsistencies() {
        List<Tuple<String, String, Double>> records = new ArrayList<>();
        records.add(new Tuple<>("AAPL", "2023-09-01", 0.22));
        records.add(new Tuple<>("AAPL", "2023-09-01", 0.22));
        records.add(new Tuple<>("MSFT", "2023-09-01", 0.56));
        records.add(new Tuple<>("GOOG", "2023-09-02", 0.00));

        List<Tuple<String, String>> expectedOutput = new ArrayList<>();
        List<Tuple<String, String>> actualOutput = checkDividendVariances(records);

        assertEquals(expectedOutput, actualOutput);
    }

    /**
     * Test case for one inconsistency in the records.
     */
    @Test
    public void testOneInconsistency() {
        List<Tuple<String, String, Double>> records = new ArrayList<>();
        records.add(new Tuple<>("AAPL", "2023-09-01", 0.22));
        records.add(new Tuple<>("AAPL", "2023-09-01", 0.23));  // Different amount
        records.add(new Tuple<>("MSFT", "2023-09-01", 0.56));
        records.add(new Tuple<>("GOOG", "2023-09-02", 0.00));

        List<Tuple<String, String>> expectedOutput = new ArrayList<>();
        expectedOutput.add(new Tuple<>("AAPL", "2023-09-01"));
        List<Tuple<String, String>> actualOutput = checkDividendVariances(records);

        assertEquals(expectedOutput, actualOutput);
    }

    /**
     * Test case for multiple inconsistencies in the records.
     */
    @Test
    public void testMultipleInconsistencies() {
        List<Tuple<String, String, Double>> records = new ArrayList<>();
        records.add(new Tuple<>("AAPL", "2023-09-01", 0.22));
        records.add(new Tuple<>("AAPL", "2023-09-01", 0.23));  // Different amount
        records.add(new Tuple<>("MSFT", "2023-09-01", 0.56));
        records.add(new Tuple<>("MSFT", "2023-09-01", 0.60));  // Different amount
        records.add(new Tuple<>("GOOG", "2023-09-02", 0.00));
        records.add(new Tuple<>("TSLA", "2023-09-03", 0.10));
        records.add(new Tuple<>("TSLA", "2023-09-03", 0.10));  // Same amount, no inconsistency
        records.add(new Tuple<>("TSLA", "2023-09-03", 0.15));  // Different amount

        List<Tuple<String, String>> expectedOutput = new ArrayList<>();
        expectedOutput.add(new Tuple<>("AAPL", "2023-09-01"));
        expectedOutput.add(new Tuple<>("MSFT", "2023-09-01"));
        expectedOutput.add(new Tuple<>("TSLA", "2023-09-03"));
        List<Tuple<String, String>> actualOutput = checkDividendVariances(records);

        assertEquals(expectedOutput, actualOutput);
    }

    /**
     * Test case for a single record.
     */
    @Test
    public void testSingleRecord() {
        List<Tuple<String, String, Double>> records = new ArrayList<>();
        records.add(new Tuple<>("AAPL", "2023-09-01", 0.22));

        List<Tuple<String, String>> expectedOutput = new ArrayList<>();
        List<Tuple<String, String>> actualOutput = checkDividendVariances(records);

        assertEquals(expectedOutput, actualOutput);
    }

    /**
     * Test case for an empty list of records.
     */
    @Test
    public void testEmptyList() {
        List<Tuple<String, String, Double>> records = new ArrayList<>();

        List<Tuple<String, String>> expectedOutput = new ArrayList<>();
        List<Tuple<String, String>> actualOutput = checkDividendVariances(records);

        assertEquals(expectedOutput, actualOutput);
    }

    // Helper class to represent a tuple
    public static class Tuple<T1, T2, T3> {
        private T1 first;
        private T2 second;
        private T3 third;

        public Tuple(T1 first, T2 second, T3 third) {
            this.first = first;
            this.second = second;
            this.third = third;
        }

        public T1 getFirst() {
            return first;
        }

        public T2 getSecond() {
            return second;
        }

        public T3 getThird() {
            return third;
        }
    }

    // Helper class to represent a tuple with two elements
    public static class Tuple<T1, T2> {
        private T1 first;
        private T2 second;

        public Tuple(T1 first, T2 second) {
            this.first = first;
            this.second = second;
        }

        public T1 getFirst() {
            return first;
        }

        public T2 getSecond() {
            return second;
        }
    }

    // Method to check for dividend variances
    public static List<Tuple<String, String>> checkDividendVariances(List<Tuple<String, String, Double>> records) {
        // Map to store dividend amounts by (ticker, exDividendDate)
        Map<Tuple<String, String>, Set<Double>> dividendMap = new HashMap<>();

        // Iterate through the records
        for (Tuple<String, String, Double> record : records) {
            String ticker = record.getFirst();
            String exDividendDate = record.getSecond();
            double dividendAmount = record.getThird();

            Tuple<String, String> key = new Tuple<>(ticker, exDividendDate);
            dividendMap.computeIfAbsent(key, k -> new HashSet<>()).add(dividendAmount);
        }

        // Find entries with more than one unique dividend amount
        List<Tuple<String, String>> result = new ArrayList<>();
        for (Map.Entry<Tuple<String, String>, Set<Double>> entry : dividendMap.entrySet()) {
            if (entry.getValue().size() > 1) {
                result.add(entry.getKey());
            }
        }

        return result;
    }
}