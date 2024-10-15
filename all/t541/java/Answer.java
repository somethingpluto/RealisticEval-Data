package org.real.temp;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class Answer {
    /**
     * Filters elements from a list based on a qualification function.
     *
     * @param unfilteredList - The list to filter.
     * @param isQualified - The function that determines if an element qualifies.
     * @return - A new list containing the elements that qualify.
     */
    public static <T> List<T> filterList(List<T> unfilteredList, Predicate<T> isQualified) {
        List<T> filteredResults = new ArrayList<>();

        // Use a for loop to iterate through each element in the unfiltered list
        for (T element : unfilteredList) {
            // Check if the current element qualifies
            if (isQualified.test(element)) {
                // If it qualifies, add it to the results list
                filteredResults.add(element);
            }
        }

        return filteredResults; // Return the filtered results
    }
}