	// Written by ChatGPT
	public static class Matrix {

		public static double[][] calculateRotationMatrix(Vec3 originalVector, Vec3 targetVector) {
			// Step 1: Calculate the Axis of Rotation
			Vec3 axis = originalVector.cross(targetVector).normalize();

			// Step 2: Calculate the Angle of Rotation
			double angle = Math
					.acos(originalVector.dot(targetVector) / (originalVector.length() * targetVector.length()));

			// Step 3: Construct the Rotation Matrix
			return calculateRotationMatrix(axis, angle);
		}
    }