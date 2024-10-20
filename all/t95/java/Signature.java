/**
 * Finds matching elements and their indices in the input array
 * based on the specified comparison function.
 *
 * @param arr - The input array to search through.
 * @param comparisonFn - The comparison function to determine matches.
 * @return - A list of objects, each containing the matched element and its index.
 */
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
public static List<MatchResult> findMatchingElements(Object[] arr, Predicate<Object> comparisonFn) {
    
}