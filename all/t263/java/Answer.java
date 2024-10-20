package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    public List<Integer> spiralTraversal(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return new ArrayList<>();
        }

        int m = matrix.length;
        int n = matrix[0].length;
        int rowStart = 0, rowEnd = m - 1;
        int colStart = 0, colEnd = n - 1;
        List<Integer> result = new ArrayList<>();

        while (rowStart <= rowEnd && colStart <= colEnd) {
            // Traverse Right along the top row
            for (int j = colStart; j <= colEnd; j++) {
                result.add(matrix[rowStart][j]);
            }
            rowStart++;

            // Traverse Down along the right column
            for (int i = rowStart; i <= rowEnd; i++) {
                result.add(matrix[i][colEnd]);
            }
            colEnd--;

            // Traverse Left along the bottom row, if still within bounds
            if (rowStart <= rowEnd) {
                for (int j = colEnd; j >= colStart; j--) {
                    result.add(matrix[rowEnd][j]);
                }
                rowEnd--;
            }

            // Traverse Up along the left column, if still within bounds
            if (colStart <= colEnd) {
                for (int i = rowEnd; i >= rowStart; i--) {
                    result.add(matrix[i][colStart]);
                }
                colStart++;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Answer answer = new Answer();
        
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        List<Integer> result = answer.spiralTraversal(matrix);
        System.out.println(result);
    }
}