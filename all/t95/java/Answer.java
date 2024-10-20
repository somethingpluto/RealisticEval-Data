package org.real.temp;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class Answer {

    /**
     * Finds matching elements and their indices in the input array
     * based on the specified comparison function.
     *
     * @param arr - The input array to search through.
     * @param comparisonFn - The comparison function to determine matches.
     * @return - A list of objects, each containing the matched element and its index.
     */
    public static List<MatchResult> findMatchingElements(Object[] arr, Predicate<Object> comparisonFn) {
        List<MatchResult> result = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            if (comparisonFn.test(arr[i])) {
                result.add(new MatchResult(arr[i], i));
            }
        }

        return result;
    }

    public static class MatchResult {
        private Object element;
        private int index;

        public MatchResult(Object element, int index) {
            this.element = element;
            this.index = index;
        }

        public Object getElement() {
            return element;
        }

        public int getIndex() {
            return index;
        }
    }

    public static void main(String[] args) {
        // Example usage
        Object[] arr = {1, 2, 3, 4, 5};
        Predicate<Object> comparisonFn = obj -> (Integer) obj > 2;

        List<MatchResult> matches = findMatchingElements(arr, comparisonFn);
        for (MatchResult match : matches) {
            System.out.println("Element: " + match.getElement() + ", Index: " + match.getIndex());
        }
    }
}