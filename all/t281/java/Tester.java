package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class Tester {

    @Test
    public void testSquaredEuclideanDistance() {
        List<Integer> vec1 = Arrays.asList(1, 2, 3);
        List<Integer> vec2 = Arrays.asList(4, 5, 6);

        int expectedDistance = 27; // (1-4)^2 + (2-5)^2 + (3-6)^2 = 9 + 9 + 9 = 27
        int actualDistance = VectorUtils.squaredEuclideanDistance(vec1, vec2);

        assertEquals(expectedDistance, actualDistance, "The squared Euclidean distance should be 27");
    }
}