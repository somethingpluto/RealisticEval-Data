package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Flattens a multi-dimensional array into a one-dimensional array.
     *
     * @param multiDimArray A multi-dimensional list (nested list).
     * @return A one-dimensional list containing all elements of the input.
     */
    public static List<Object> flattenArray(List<?> multiDimArray) {
        List<Object> flatList = new ArrayList<>();

        flatten(multiDimArray, flatList);
        return flatList;
    }

    private static void flatten(List<?> subArray, List<Object> flatList) {
        for (Object item : subArray) {
            if (item instanceof List) {
                // Recursively flatten if the current item is a list
                flatten((List<?>) item, flatList);
            } else {
                // Append the non-list item to the flatList
                flatList.add(item);
            }
        }
    }

    public static void main(String[] args) {
        // Example usage
        List<Object> multiDimArray = new ArrayList<>();
        multiDimArray.add(new ArrayList<>(List.of(1, 2, new ArrayList<>(List.of(3)))));
        multiDimArray.add(new ArrayList<>(List.of(4, 5)));
        multiDimArray.add(6);

        List<Object> flatList = flattenArray(multiDimArray);
        System.out.println(flatList);  // Output: [1, 2, 3, 4, 5, 6]
    }
}