package org.real.temp;

import java.util.List;

public class Answer {

    public static List<List<Integer>> matrixMultiply(List<List<Integer>> matrixA, List<List<Integer>> matrixB) {
        int rowsA = matrixA.size();
        int colsA = matrixA.get(0).size();
        int colsB = matrixB.get(0).size();

        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < rowsA; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < colsB; j++) {
                int sum = 0;
                for (int k = 0; k < colsA; k++) {
                    sum += matrixA.get(i).get(k) * matrixB.get(k).get(j);
                }
                row.add(sum);
            }
            result.add(row);
        }

        return result;
    }
}