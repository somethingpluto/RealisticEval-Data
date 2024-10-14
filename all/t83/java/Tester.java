public class Tester {

    /**
     * Rotates the elements of the list to the left by one position. The first element
     * is moved to the end of the list, and all other elements are shifted one position to the left.
     *
     * @param elements A list of integers to be rotated.
     * @return The rotated list with elements shifted to the left by one position.
     */
    private static List<Integer> rotateListElements(List<Integer> elements) {
        if (elements.size() > 1) {
            List<Integer> rotated = new ArrayList<>(elements.subList(1, elements.size()));
            rotated.add(elements.get(0));
            return rotated;
        }
        return elements;
    }

    @Test
    public void testBasicRotation() {
        List<Integer> originalList = new ArrayList<>(Arrays.asList(1, 2, 3, 4));
        List<Integer> expectedList = new ArrayList<>(Arrays.asList(2, 3, 4, 1));
        assertEquals(expectedList, rotateListElements(originalList), "Should rotate the list elements correctly");
    }

    @Test
    public void testSingleElementList() {
        List<Integer> originalList = new ArrayList<>(Arrays.asList(10));
        List<Integer> expectedList = new ArrayList<>(Arrays.asList(10));
        assertEquals(expectedList, rotateListElements(originalList), "Single element list should remain unchanged");
    }

    @Test
    public void testEmptyList() {
        List<Integer> originalList = new ArrayList<>();
        List<Integer> expectedList = new ArrayList<>();
        assertEquals(expectedList, rotateListElements(originalList), "Empty list should remain unchanged");
    }

    @Test
    public void testTwoElementList() {
        List<Integer> originalList = new ArrayList<>(Arrays.asList(5, 9));
        List<Integer> expectedList = new ArrayList<>(Arrays.asList(9, 5));
        assertEquals(expectedList, rotateListElements(originalList), "Should correctly rotate a two-element list");
    }

    @Test
    public void testLargeList() {
        List<Integer> largeList = new ArrayList<>();
        for (int i = 1; i <= 1000; i++) {
            largeList.add(i);
        }
        List<Integer> expectedList = new ArrayList<>(largeList.subList(1, largeList.size()));
        expectedList.add(largeList.get(0));
        assertEquals(expectedList, rotateListElements(largeList), "Should correctly rotate a large list");
    }
}