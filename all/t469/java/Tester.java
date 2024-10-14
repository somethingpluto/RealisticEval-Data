package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import java.awt.geom.AffineTransform;
import java.awt.geom.Point2D;

public class Tester {

    @Test
    public void testGetScale() {
        // Define a sample 3x3 affine transformation matrix
        double[][] matrix = {
            {2.0, 0.0, 0.0},
            {0.0, 3.0, 0.0},
            {0.0, 0.0, 1.0}
        };

        // Convert the matrix to an AffineTransform object
        AffineTransform transform = new AffineTransform();
        transform.setTransform(
            matrix[0][0], matrix[0][1], matrix[0][2],
            matrix[1][0], matrix[1][1], matrix[1][2]
        );

        // Get the scale factors
        Point2D.Double scale = new Point2D.Double();
        transform.getScale(scale);

        // Check if the scale factors are correct
        assertEquals(2.0, scale.x, "Scale factor along X-axis should be 2.0");
        assertEquals(3.0, scale.y, "Scale factor along Y-axis should be 3.0");
    }
}
