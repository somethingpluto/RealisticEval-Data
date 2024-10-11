package org.real.temp;

import java.util.Arrays;
import java.util.List;

public class Answer {

    public static List<Integer> decompose(int n, int[] shape) throws IllegalArgumentException {
        // Check if n is within the valid range
        int totalElements = 1;
        for (int dim : shape) {
            totalElements *= dim;
        }

        if (n < 0 || n >= totalElements) {
            throw new IllegalArgumentException("Index " + n + " is out of bounds for the array with shape " + Arrays.toString(shape));
        }

        // Convert the flat index to a multidimensional index
        List<Integer> result = new ArrayList<>();
        int currentDim = n;
        for (int i = shape.length - 1; i >= 0; --i) {
            result.add(0, currentDim % shape[i]);
            currentDim /= shape[i];
        }

        return result;
    }
}