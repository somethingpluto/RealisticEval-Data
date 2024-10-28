package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.List;
import java.util.ArrayList;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testStandardMatrices() {
        List<List<Integer>> mat1 = new ArrayList<>();
        mat1.add(new ArrayList<>(List.of(1, 2)));
        mat1.add(new ArrayList<>(List.of(3, 4)));

        List<List<Integer>> mat2 = new ArrayList<>();
        mat2.add(new ArrayList<>(List.of(5, 6)));
        mat2.add(new ArrayList<>(List.of(7, 8)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(19, 22)));
        expected.add(new ArrayList<>(List.of(43, 50)));

        assertEquals("Should correctly multiply standard matrices",expected, matrixMultiply(mat1, mat2));
    }

    @Test
    public void testIdentityMatrix() {
        List<List<Integer>> mat1 = new ArrayList<>();
        mat1.add(new ArrayList<>(List.of(1, 0)));
        mat1.add(new ArrayList<>(List.of(0, 1)));

        List<List<Integer>> mat2 = new ArrayList<>();
        mat2.add(new ArrayList<>(List.of(5, 6)));
        mat2.add(new ArrayList<>(List.of(7, 8)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(5, 6)));
        expected.add(new ArrayList<>(List.of(7, 8)));

        assertEquals("Multiplying by the identity matrix should yield the answer matrix",expected, matrixMultiply(mat1, mat2));
    }

    @Test
    public void testZeroMatrix() {
        List<List<Integer>> mat1 = new ArrayList<>();
        mat1.add(new ArrayList<>(List.of(0, 0)));
        mat1.add(new ArrayList<>(List.of(0, 0)));

        List<List<Integer>> mat2 = new ArrayList<>();
        mat2.add(new ArrayList<>(List.of(5, 6)));
        mat2.add(new ArrayList<>(List.of(7, 8)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(0, 0)));
        expected.add(new ArrayList<>(List.of(0, 0)));

        assertEquals("Multiplying by the zero matrix should yield a zero matrix",expected, matrixMultiply(mat1, mat2));
    }

    @Test
    public void testSquareMatrixMultiplication() {
        List<List<Integer>> mat1 = new ArrayList<>();
        mat1.add(new ArrayList<>(List.of(1, 2)));
        mat1.add(new ArrayList<>(List.of(3, 4)));

        List<List<Integer>> mat2 = new ArrayList<>();
        mat2.add(new ArrayList<>(List.of(5, 6)));
        mat2.add(new ArrayList<>(List.of(7, 8)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(19, 22)));
        expected.add(new ArrayList<>(List.of(43, 50)));

        assertEquals("The multiplication of two square matrices should yield the correct product",expected, matrixMultiply(mat1, mat2));
    }

    @Test
    public void testLargeIdentityMatrix() {
        List<List<Integer>> mat1 = new ArrayList<>();
        mat1.add(new ArrayList<>(List.of(1, 0, 0)));
        mat1.add(new ArrayList<>(List.of(0, 1, 0)));
        mat1.add(new ArrayList<>(List.of(0, 0, 1)));

        List<List<Integer>> mat2 = new ArrayList<>();
        mat2.add(new ArrayList<>(List.of(5, 6, 7)));
        mat2.add(new ArrayList<>(List.of(8, 9, 10)));
        mat2.add(new ArrayList<>(List.of(11, 12, 13)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(5, 6, 7)));
        expected.add(new ArrayList<>(List.of(8, 9, 10)));
        expected.add(new ArrayList<>(List.of(11, 12, 13)));

        assertEquals("Multiplying by the larger identity matrix should yield the answer matrix",expected, matrixMultiply(mat1, mat2));
    }
}