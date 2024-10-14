import org.apache.commons.math3.geometry.euclidean.threed.Vector3D;
import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.RealMatrix;

/**
 * Create a pose matrix representing a rotation about a given axis.
 *
 * @param angleDeg Rotation angle in degrees.
 * @param axis     Axis to rotate about, must be one of 'X', 'Y', or 'Z'.
 * @return A 4x4 pose matrix representing the rotation.
 */
public class PoseMatrixCreator {

    public static RealMatrix createRotMatrix(double angleDeg, String axis) {
        // Implementation goes here
    }
}
