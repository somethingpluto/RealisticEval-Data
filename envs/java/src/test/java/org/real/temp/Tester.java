package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void testStandardVectors() {
        List<Integer> vec1 = Arrays.asList(1, 2, 3);
        List<Integer> vec2 = Arrays.asList(4, 5, 6);
        int expectedResult = 27;  // (3^2 + 3^2 + 3^2)
        int result = squaredEuclideanDistance(vec1, vec2);
        assertEquals(expectedResult, result);
    }

    @Test
    public void testVectorsWithZeros() {
        List<Integer> vec1 = Arrays.asList(0, 0, 0);
        List<Integer> vec2 = Arrays.asList(0, 0, 0);
        int expectedResult = 0;
        int result = squaredEuclideanDistance(vec1, vec2);
        assertEquals(expectedResult, result);
    }

    @Test
    public void testVectorsWithNegativeValues() {
        List<Integer> vec1 = Arrays.asList(-1, -2, -3);
        List<Integer> vec2 = Arrays.asList(-4, -5, -6);
        int expectedResult = 27;  // (3^2 + 3^2 + 3^2)
        int result = squaredEuclideanDistance(vec1, vec2);
        assertEquals(expectedResult, result);
    }

    @Test
    public void testSingleElementVectors() {
        List<Integer> vec1 = Arrays.asList(5);
        List<Integer> vec2 = Arrays.asList(-5);
        int expectedResult = 100;  // (10^2)
        int result = squaredEuclideanDistance(vec1, vec2);
        assertEquals(expectedResult, result);
    }

    // The squaredEuclideanDistance method implementation
    private int squaredEuclideanDistance(List<Integer> vec1, List<Integer> vec2) {
        if (vec1.size() != vec2.size()) {
            throw new IllegalArgumentException("Vectors must be of the same length");
        }

        int distanceSquared = 0;
        for (int i = 0; i < vec1.size(); i++) {
            int diff = vec1.get(i) - vec2.get(i);
            distanceSquared += diff * diff;
        }
        return distanceSquared;
    }
}