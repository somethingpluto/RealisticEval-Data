package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.List;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testIdentityMatrix() {
        // Testing the power function with an identity matrix
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(new ArrayList<>(List.of(1, 0)));
        matrix.add(new ArrayList<>(List.of(0, 1)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(1, 0)));
        expected.add(new ArrayList<>(List.of(0, 1)));

        List<List<Integer>> result = power(matrix, 1);
        assertEquals(expected, result);
    }

    @Test
    public void testZeroPower() {
        // Testing matrix to the power of zero (should return identity)
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(new ArrayList<>(List.of(2, 3)));
        matrix.add(new ArrayList<>(List.of(1, 4)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(1, 0)));
        expected.add(new ArrayList<>(List.of(0, 1)));

        List<List<Integer>> result = power(matrix, 0);
        assertEquals(expected, result);
    }

    @Test
    public void testPositivePower() {
        // Testing matrix to a positive power
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(new ArrayList<>(List.of(2, 1)));
        matrix.add(new ArrayList<>(List.of(1, 3)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(5, 5)));
        expected.add(new ArrayList<>(List.of(5, 10)));  // This is the result of matrix^2

        List<List<Integer>> result = power(matrix, 2);
        assertEquals(expected, result);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNegativePower() {
        // Testing matrix to a negative power (should raise IllegalArgumentException)
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(new ArrayList<>(List.of(2, 1)));
        matrix.add(new ArrayList<>(List.of(1, 3)));

        power(matrix, -1);
    }
}