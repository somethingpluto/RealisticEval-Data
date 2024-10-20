package org.real.temp;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Answer {

    /**
     * Decompose a flat index `n` into a multidimensional index based on the given shape.
     *
     * @param n     Flat index (non-negative integer).
     * @param shape Tuple representing the dimensions of the multi-dimensional array.
     * @return Tuple representing the multidimensional index corresponding to `n`.
     * @throws IllegalArgumentException If `n` is out of bounds for the array defined by `shape`.
     */
    public static List<Integer> decompose(int n, int[] shape) {
        // Calculate the total size of the array
        int size = 1;
        for (int dim : shape) {
            size *= dim;
        }

        // Check if the index is within bounds
        if (n < 0 || n >= size) {
            throw new IllegalArgumentException("Index out of bounds");
        }

        // Decompose the index
        List<Integer> result = new ArrayList<>();
        for (int i = shape.length - 1; i >= 0; i--) {
            result.add(n % shape[i]);
            n /= shape[i];  // Update n by integer division
        }

        // Reverse the result to match the original shape order
        Collections.reverse(result);

        return result;
    }

    public static void main(String[] args) {
        int[] shape = {3, 4, 5};
        int n = 27;
        List<Integer> result = decompose(n, shape);
        System.out.println(result);  // Example output: [1, 1, 2]
    }
}