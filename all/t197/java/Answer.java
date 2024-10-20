
package org.real.temp;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Simulates the Josephus problem using a list to represent the circle of people.
     *
     * @param n The number of people in the circle (1 to n).
     * @param k The step count (every k-th person will be eliminated).
     * @return The position of the last person remaining (1-indexed).
     */
    public static int josephus(int n, int k) {
        // Step 1: Create a list to represent the people in the circle
        List<Integer> people = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            people.add(i);  // Create a list of people from 1 to n
        }

        int index = 0;  // Start from the first person

        // Step 2: Eliminate people until only one remains
        while (people.size() > 1) {
            // Step 3: Find the index of the person to eliminate
            index = (index + k - 1) % people.size();  // -1 to adjust for zero-based index
            int eliminatedPerson = people.remove(index);  // Eliminate that person
            System.out.println("Eliminated: " + eliminatedPerson + ", Remaining: " + people);
        }

        // Step 4: Return the position of the last remaining person
        return people.get(0);  // The last remaining person
    }

    public static void main(String[] args) {
        // Test the josephus function
        int lastPerson = josephus(7, 3);
        System.out.println("The last remaining person is at position: " + lastPerson);
    }
}
