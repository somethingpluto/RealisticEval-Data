package org.real.temp;

public class Answer {

    /**
     * Performs matrix-vector multiplication.
     * 
     * @param matrix The matrix as a 2D array.
     * @param vector The vector as a 1D array.
     * @return The resulting vector after multiplication.
     */
    public static double[] matrixVectorMultiplication(double[][] matrix, double[] vector) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        
        if (cols != vector.length) {
            throw new IllegalArgumentException("Matrix columns must match vector length.");
        }
        
        double[] result = new double[rows];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i] += matrix[i][j] * vector[j];
            }
        }
        
        return result;
    }

    public static void main(String[] args) {
        // Example usage
        double[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        double[] vector = {1, 0, 1};
        
        double[] result = matrixVectorMultiplication(matrix, vector);
        
        // Print the result
        System.out.println("Result:");
        for (double value : result) {
            System.out.println(value);
        }
    }
}