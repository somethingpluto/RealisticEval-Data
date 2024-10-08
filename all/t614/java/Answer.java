package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Calculates the average difference between consecutive integers in the provided list.
     *
     * @param numbers a list of integers
     * @return the average difference, or 0 if there are fewer than 2 integers
     */
    public static double calculateAverageDifference(List<Integer> numbers) {
        if (numbers == null || numbers.size() < 2) {
            return 0.0; // Not enough data to calculate differences
        }

        List<Integer> differences = new ArrayList<>();

        // Calculate differences from the previous data
        for (int i = 1; i < numbers.size(); i++) {
            int difference = numbers.get(i) - numbers.get(i - 1);
            differences.add(difference);
        }

        // Calculate the average of the differences
        double sum = 0.0;
        for (Integer diff : differences) {
            sum += diff;
        }

        return sum / differences.size(); // Return average
    }

    // Example usage
    public static void main(String[] args) {
        List<Integer> sampleNumbers = List.of(10, 20, 15, 30, 25);
        double averageDifference = calculateAverageDifference(sampleNumbers);
        System.out.println("Average Difference: " + averageDifference);
    }
}