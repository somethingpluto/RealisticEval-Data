package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertTrue;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testStandardVectors() {
        List<Double> vec1 = Arrays.asList(1.0, 2.0, 3.0);
        List<Double> vec2 = Arrays.asList(4.0, 5.0, 6.0);
        double expectedResult = 27.0;  // (3^2 + 3^2 + 3^2)
        double result = squaredEuclideanDistance(vec1, vec2);
        assertTrue(expectedResult ==result );
    }

    @Test
    public void testVectorsWithZeros() {
        List<Double> vec1 = Arrays.asList(0.0, 0.0, 0.0);
        List<Double> vec2 = Arrays.asList(0.0, 0.0, 0.0);
        double expectedResult = 0.0;
        double result = squaredEuclideanDistance(vec1, vec2);
        assertTrue(expectedResult ==result );
    }

    @Test
    public void testVectorsWithNegativeValues() {
        List<Double> vec1 = Arrays.asList(-1.0, -2.0, -3.0);
        List<Double> vec2 = Arrays.asList(-4.0, -5.0, -6.0);
        double expectedResult = 27.0;  // (3^2 + 3^2 + 3^2)
        double result = squaredEuclideanDistance(vec1, vec2);
        assertTrue(expectedResult ==result );
    }

    @Test
    public void testSingleElementVectors() {
        List<Double> vec1 = Arrays.asList(5.0);
        List<Double> vec2 = Arrays.asList(-5.0);
        double expectedResult = 100.0;  // (10^2)
        double result = squaredEuclideanDistance(vec1, vec2);
        assertTrue(expectedResult ==result );
    }
}