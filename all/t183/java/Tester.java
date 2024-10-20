package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testcase1() {
        // Test Case 1: The ray intersects the circle at two points
        Ray ray1 = new Ray(new Point(0, 0), new Point(1, 1)); // Origin at (0, 0), direction (1, 1)
        Circle circle1 = new Circle(new Point(3, 3), 2); // Circle center at (3, 3), radius 2
        assertTrue(intersects(ray1, circle1));

    }

    @Test
    public void testcase2(){
        // Test Case 2: The ray is tangent to the circle (one intersection point)
        Ray ray2 = new Ray(new Point(2, 0), new Point(0, 1)); // Origin at (2, 0), direction (0, 1)
        Circle circle2 = new Circle(new Point(2, 2), 1); // Circle center at (2, 2), radius 1
        assertTrue(intersects(ray2, circle2));
    }
    @Test
    public void testcase3(){
        // Test Case 3: The ray starts inside the circle (one intersection point)
        Ray ray3 = new Ray(new Point(2, 2), new Point(1, 0)); // Origin at (2, 2), direction (1, 0)
        Circle circle3 = new Circle(new Point(3, 2), 1); // Circle center at (3, 2), radius 1
        assertTrue(intersects(ray3, circle3));

    }
    @Test
    public void testcase4(){
        // Test Case 4: The ray originates outside and goes away from the circle (no intersection)
        Ray ray4 = new Ray(new Point(5, 5), new Point(1, 0)); // Origin at (5, 5), direction (1, 0)
        Circle circle4 = new Circle(new Point(3, 3), 1); // Circle center at (3, 3), radius 1
        assertFalse(intersects(ray4, circle4));
    }
    @Test
    public void testcase5(){
        // Test Case 5: The ray is parallel to the line connecting the center of the circle and is outside (no intersection)
        Ray ray5 = new Ray(new Point(0, 3), new Point(1, 0)); // Origin at (0, 3), direction (1, 0)
        Circle circle5 = new Circle(new Point(3, 3), 1); // Circle center at (3, 3), radius 1
        assertTrue(intersects(ray5, circle5));

    }
    @Test
    public void testcase6(){

        // Test Case 6: The ray intersects the circle at one point when passing through the center
        Ray ray6 = new Ray(new Point(3, 0), new Point(0, 1)); // Origin at (3, 0), direction (0, 1)
        Circle circle6 = new Circle(new Point(3, 3), 3); // Circle center at (3, 3), radius 3
        assertTrue(intersects(ray6, circle6));
    }
}