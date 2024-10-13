package org.real.temp;

import org.junit.jupiter.api.Test; // JUnit 5 Test annotation
import static org.junit.jupiter.api.Assertions.assertEquals; // JUnit 5 assertion method


public class Tester {

    @Test
    public void testBasicArray() {
        // Test with a basic array where multiple removals are needed.
        assertEquals(3, minRemovalsToMakeUnique(List.of(3, 3, 1, 2, 2, 1)));
    }

    @Test
    public void testAllIdentical() {
        // Test an array where all elements are identical.
        assertEquals(3, minRemovalsToMakeUnique(List.of(4, 4, 4, 4)));
    }

    @Test
    public void testAllUnique() {
        // Test an array where all elements are already unique.
        assertEquals(0, minRemovalsToMakeUnique(List.of(1, 2, 3, 4)));
    }

    @Test
    public void testEmptyArray() {
        // Test an empty array.
        assertEquals(0, minRemovalsToMakeUnique(List.of()));
    }

    @Test
    public void testComplexCase() {
        // Test a more complex case with a larger array.
        assertEquals(6, minRemovalsToMakeUnique(List.of(1, 2, 2, 3, 3, 3, 4, 4, 4, 4)));
    }

    // Method to be tested
    private int minRemovalsToMakeUnique(List<Integer> nums) {
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
}