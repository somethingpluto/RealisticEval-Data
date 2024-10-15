package org.real.temp;
import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Iterates through the array of elements until the first null is encountered,
     * returning a new list that includes all elements before the null.
     *
     * @param array - The array to iterate through.
     * @returns - A new list containing elements before the first null.
     */
    public static List<Object> elementsBeforeNull(Object[] array) {
        List<Object> result = new ArrayList<>(); // Initialize an empty list to hold the result

        for (Object element : array) {
            if (element == null) {
                break; // Exit the loop if null is encountered
            }
            result.add(element); // Add the current element to the result list
        }

        return result; // Return the result list
    }
}