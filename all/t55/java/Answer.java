package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Calculates the minimum number of removals needed to make all elements in the list unique.
     * 
     * @param nums The list of integers.
     * @return The minimum number of removals required.
     */
    public static int minRemovalsToMakeUnique(List<Integer> nums) {
        List<Integer> numbers = new ArrayList<>();
        int minimumDistinct = 0;
        
        for (int number : nums) {
            if (numbers.contains(number)) {
                minimumDistinct++;
                numbers.remove(Integer.valueOf(number));
            }
            numbers.add(number);
        }
        
        return minimumDistinct;
    }

    public static void main(String[] args) {
        // Example usage
        List<Integer> nums = List.of(1, 2, 2, 3, 4, 4, 5);
        System.out.println(minRemovalsToMakeUnique(nums)); // Output will be the minimum number of removals
    }
}