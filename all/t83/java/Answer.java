package org.real.temp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Answer {

    /**
     * Rotate the elements of the list to the left by one position. The first element
     * is moved to the end of the list, and all other elements are shifted one position to the left.
     *
     * @param elements A list of integers to be rotated.
     * @return The rotated list with elements shifted to the left by one position.
     */
    public static List<Integer> rotateListElements(List<Integer> elements) {
        if (elements.size() > 1) {
            List<Integer> rotated = new ArrayList<>(elements.subList(1, elements.size()));
            rotated.add(elements.get(0));
            return rotated;
        }
        return elements;
    }

    /**
     * Rotate the elements of the list, moving the first element to the end and shifting all others forward.
     *
     * @param elements The list of elements to rotate.
     * @return The list after rotation.
     */
    public static List<Integer> rotateList(List<Integer> elements) {
        if (elements.isEmpty()) {
            return elements; // Return the list as is if it's empty
        }

        // Move the first element to the last and shift others forward
        List<Integer> rotatedList = new ArrayList<>(elements.subList(1, elements.size()));
        rotatedList.add(elements.get(0));

        return rotatedList;
    }

    public static void main(String[] args) {
        List<Integer> elements = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> rotatedElements = rotateList(elements);
        System.out.println(rotatedElements); // Output: [2, 3, 4, 5, 1]
    }
}
