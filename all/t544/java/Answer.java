package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Filters out all even numbers from an array.
     *
     * @param array - The array of numbers to filter.
     * @return - A new list containing only the odd numbers.
     */
    public static List<Integer> filterOutEvenNumbers(int[] array) {
        List<Integer> oddNumbers = new ArrayList<>();
        for (int num : array) {
            if (num % 2 != 0) {
                oddNumbers.add(num);
            }
        }
        return oddNumbers;
    }
}