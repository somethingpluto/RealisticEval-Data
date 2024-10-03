		// Written by ChatGPT
		public static double[][] multiplyMatrix(double[][] matrixA, double[][] matrixB) {
			int rowsA = matrixA.length;
			int colsA = matrixA[0].length;
			int colsB = matrixB[0].length;

			if (matrixB.length != colsA) {
				throw new IllegalArgumentException("Incompatible matrix dimensions for multiplication");
			}

			double[][] result = new double[rowsA][colsB];

			for (int i = 0; i < rowsA; i++) {
				for (int j = 0; j < colsB; j++) {
					for (int k = 0; k < colsA; k++) {
						result[i][j] += matrixA[i][k] * matrixB[k][j];
					}
				}
			}

			return result;

		}