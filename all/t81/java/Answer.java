package org.real.temp;

import java.util.List;
import java.util.NoSuchElementException;

public class Answer {

    /**
     * Finds and returns the element from the given list that is closest to the specified target value.
     *
     * @param target   The target number to which we want to find the closest element.
     * @param elements A list of numerical elements from which the closest element is to be found.
     * @return The element from the list that is closest to the target value.
     */
    public static Number findClosestElement(Number target, List<Number> elements) {
        if (elements.isEmpty()) {
            throw new NoSuchElementException("The list of elements cannot be empty.");
        }

        return elements.stream()
                .min((x1, x2) -> Double.compare(Math.abs(x1.doubleValue() - target.doubleValue()), Math.abs(x2.doubleValue() - target.doubleValue())))
                .orElseThrow(() -> new NoSuchElementException("No value present"));
    }

    public static void main(String[] args) {
        // Example usage
        List<Number> elements = List.of(1, 2, 3, 4, 5);
        Number target = 3.5;
        Number closestElement = findClosestElement(target, elements);
        System.out.println("Closest element: " + closestElement);
    }
}