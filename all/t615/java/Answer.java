package org.real.temp;

import java.util.List;

public class Answer {

    public static double calculate(List<Integer> values, int period) {
        // Check if the number of values is less than the specified period
        if (values == null || values.size() < period || period <= 0) {
            return Double.NaN;  // Return NaN for invalid input
        }

        double sum = 0;  // Initialize the sum
        // Calculate the sum of the last 'period' values
        for (int i = values.size() - period; i < values.size(); i++) {
            sum += values.get(i);
        }

        // Return the average of the last 'period' values
        return sum / period;
    }
}