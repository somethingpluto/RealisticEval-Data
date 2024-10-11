package org.real.temp;

import java.util.List;

public class Answer {
    public static int squaredEuclideanDistance(List<Integer> vec1, List<Integer> vec2) {
        if (vec1.size() != vec2.size()) {
            throw new IllegalArgumentException("Vectors must have the same size");
        }

        int sum = 0;
        for (int i = 0; i < vec1.size(); i++) {
            int diff = vec1.get(i) - vec2.get(i);
            sum += diff * diff;
        }

        return sum;
    }
}