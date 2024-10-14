package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Test class for checking if a point is inside a triangle.
 */
public class Tester {

    /**
     * Test case where the point is inside the triangle.
     */
    @Test
    public void testPointInsideTriangle() {
        double[] triangleVertices = {0, 0, 5, 0, 2.5, 5};
        double px = 2.5;
        double py = 2;  // Inside the triangle

        assertTrue(isPointInsideTriangle(px, py, triangleVertices[0], triangleVertices[1],
                                         triangleVertices[2], triangleVertices[3],
                                         triangleVertices[4], triangleVertices[5]));
    }

    /**
     * Test case where the point is on the edge of the triangle.
     */
    @Test
    public void testPointOnEdge() {
        double[] triangleVertices = {0, 0, 5, 0, 2.5, 5};
        double px = 2.5;
        double py = 0;  // On the edge of the triangle

        assertTrue(isPointInsideTriangle(px, py, triangleVertices[0], triangleVertices[1],
                                         triangleVertices[2], triangleVertices[3],
                                         triangleVertices[4], triangleVertices[5]));
    }

    /**
     * Test case where the point is outside the triangle.
     */
    @Test
    public void testPointOutsideTriangle() {
        double[] triangleVertices = {0, 0, 5, 0, 2.5, 5};
        double px = 6;
        double py = 2;  // Outside the triangle

        assertFalse(isPointInsideTriangle(px, py, triangleVertices[0], triangleVertices[1],
                                          triangleVertices[2], triangleVertices[3],
                                          triangleVertices[4], triangleVertices[5]));
    }

    /**
     * Test case where the point is at one of the triangle's vertices.
     */
    @Test
    public void testPointAtVertex() {
        double[] triangleVertices = {0, 0, 5, 0, 2.5, 5};
        double px = 0;
        double py = 0;  // At the vertex of the triangle

        assertTrue(isPointInsideTriangle(px, py, triangleVertices[0], triangleVertices[1],
                                         triangleVertices[2], triangleVertices[3],
                                         triangleVertices[4], triangleVertices[5]));
    }
}