package org.real.temp;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Answer {

    /**
     * Check for ticker symbols with the same ex-dividend date but different dividend amounts.
     *
     * @param records A list of tuples where each tuple contains (ticker, exDividendDate, dividendAmount).
     * @return A list of tuples where each tuple contains (ticker, exDividendDate) that have different dividend amounts.
     */
    public static List<Tuple<String, String>> checkDividendVariances(List<Tuple<String, String, Integer>> records) {
        // Map to store dividend amounts by (ticker, exDividendDate)
        Map<Tuple<String, String>, Set<Integer>> dividendMap = new HashMap<>();

        // Iterate through the records
        for (Tuple<String, String, Integer> record : records) {
            String ticker = record.getFirst();
            String exDividendDate = record.getSecond();
            int dividendAmount = record.getThird();

            Tuple<String, String> key = new Tuple<>(ticker, exDividendDate);
            dividendMap.computeIfAbsent(key, k -> new HashSet<>()).add(dividendAmount);
        }

        // Find entries with more than one unique dividend amount
        List<Tuple<String, String>> result = new ArrayList<>();
        for (Map.Entry<Tuple<String, String>, Set<Integer>> entry : dividendMap.entrySet()) {
            if (entry.getValue().size() > 1) {
                result.add(entry.getKey());
            }
        }

        return result;
    }

    // Helper class to represent a tuple
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

    // Helper class to represent a tuple with three elements
    public static class Tuple<T1, T2, T3> extends Tuple<T1, T2> {
        private T3 third;

        public Tuple(T1 first, T2 second, T3 third) {
            super(first, second);
            this.third = third;
        }

        public T3 getThird() {
            return third;
        }
    }

    public static void main(String[] args) {
        // Example usage
        List<Tuple<String, String, Integer>> records = new ArrayList<>();
        records.add(new Tuple<>("AAPL", "2023-01-01", 100));
        records.add(new Tuple<>("AAPL", "2023-01-01", 150));
        records.add(new Tuple<>("GOOGL", "2023-01-02", 200));
        records.add(new Tuple<>("MSFT", "2023-01-01", 120));
        records.add(new Tuple<>("MSFT", "2023-01-01", 120));

        List<Tuple<String, String>> result = checkDividendVariances(records);
        for (Tuple<String, String> tuple : result) {
            System.out.println(tuple.getFirst() + ", " + tuple.getSecond());
        }
    }
}