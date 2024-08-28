package com.real.t176;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;

import com.real.t176.Adapted.*;


public class TestClass {
    @Test
    public void testFindKNearestNeighbors_SimpleCase() {
        Adapted knn = new Adapted();
        Adapted.Point[] points = {
                new Adapted.Point(1, 2),
                new Adapted.Point(3, 4),
                new Adapted.Point(1, -1),
                new Adapted.Point(5, 2)
        };
        Adapted.Point queryPoint = new Adapted.Point(2, 2);
        int k = 2;

        Adapted.Point[] result = knn.findKNearestNeighbors(points, queryPoint, k);

        assertEquals(2, result.length);
        assertTrue(containsPoint(result, new Adapted.Point(1, 2)));
        assertTrue(containsPoint(result, new Adapted.Point(3, 4)));
    }

    @Test
    public void testFindKNearestNeighbors_ExactMatch() {
        Adapted knn = new Adapted();
        Adapted.Point[] points = {
                new Adapted.Point(1, 2),
                new Adapted.Point(2, 2),
                new Adapted.Point(3, 3)
        };
        Adapted.Point queryPoint = new Adapted.Point(2, 2);
        int k = 1;

        Adapted.Point[] result = knn.findKNearestNeighbors(points, queryPoint, k);

        assertEquals(1, result.length);
        assertEquals(2.0, result[0].x, 0.001);
        assertEquals(2.0, result[0].y, 0.001);
    }

    @Test
    public void testFindKNearestNeighbors_LargerK() {
        Adapted knn = new Adapted();
        Adapted.Point[] points = {
                new Adapted.Point(1, 2),
                new Adapted.Point(3, 4),
                new Adapted.Point(1, -1),
                new Adapted.Point(5, 2)
        };
        Adapted.Point queryPoint = new Adapted.Point(2, 2);
        int k = 5;  // k is larger than the number of points

        Adapted.Point[] result = knn.findKNearestNeighbors(points, queryPoint, k);

        assertEquals(4, result.length);
    }

    @Test
    public void testFindKNearestNeighbors_EmptyPoints() {
        Adapted knn = new Adapted();
        Adapted.Point[] points = {};
        Adapted.Point queryPoint = new Adapted.Point(2, 2);
        int k = 3;

        Adapted.Point[] result = knn.findKNearestNeighbors(points, queryPoint, k);

        assertEquals(0, result.length);
    }

    @Test
    public void testFindKNearestNeighbors_AllPointsEquidistant() {
        Adapted knn = new Adapted();
        Adapted.Point[] points = {
                new Adapted.Point(2, 3),
                new Adapted.Point(3, 2),
                new Adapted.Point(1, 2),
                new Adapted.Point(2, 1)
        };
        Adapted.Point queryPoint = new Adapted.Point(2, 2);
        int k = 2;

        Adapted.Point[] result = knn.findKNearestNeighbors(points, queryPoint, k);

        assertEquals(2, result.length);
        assertTrue(containsPoint(result, new Adapted.Point(2, 3)));
        assertTrue(containsPoint(result, new Adapted.Point(3, 2)));
    }

    private boolean containsPoint(Adapted.Point[] points, Adapted.Point point) {
        for (Adapted.Point p : points) {
            if (Math.abs(p.x - point.x) < 0.001 && Math.abs(p.y - point.y) < 0.001) {
                return true;
            }
        }
        return false;
    }
}
