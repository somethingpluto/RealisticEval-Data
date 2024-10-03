package org.real.temp;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.real.temp.*;

public class Tester {
    @Test
    public void testFindKNearestNeighbors_SimpleCase() {
        Answer knn = new Answer();
        Answer.Point[] points = {
                new Answer.Point(1, 2),
                new Answer.Point(3, 4),
                new Answer.Point(1, -1),
                new Answer.Point(5, 2)
        };
        Answer.Point queryPoint = new Answer.Point(2, 2);
        int k = 2;

        Answer.Point[] result = knn.findKNearestNeighbors(points, queryPoint, k);

        assertEquals(2, result.length);
        assertTrue(containsPoint(result, new Answer.Point(1, 2)));
        assertTrue(containsPoint(result, new Answer.Point(3, 4)));
    }

    @Test
    public void testFindKNearestNeighbors_ExactMatch() {
        Answer knn = new Answer();
        Answer.Point[] points = {
                new Answer.Point(1, 2),
                new Answer.Point(2, 2),
                new Answer.Point(3, 3)
        };
        Answer.Point queryPoint = new Answer.Point(2, 2);
        int k = 1;

        Answer.Point[] result = knn.findKNearestNeighbors(points, queryPoint, k);

        assertEquals(1, result.length);
        assertEquals(2.0, result[0].x, 0.001);
        assertEquals(2.0, result[0].y, 0.001);
    }

    @Test
    public void testFindKNearestNeighbors_LargerK() {
        Answer knn = new Answer();
        Answer.Point[] points = {
                new Answer.Point(1, 2),
                new Answer.Point(3, 4),
                new Answer.Point(1, -1),
                new Answer.Point(5, 2)
        };
        Answer.Point queryPoint = new Answer.Point(2, 2);
        int k = 5;  // k is larger than the number of points

        Answer.Point[] result = knn.findKNearestNeighbors(points, queryPoint, k);

        assertEquals(4, result.length);
    }

    @Test
    public void testFindKNearestNeighbors_EmptyPoints() {
        Answer knn = new Answer();
        Answer.Point[] points = {};
        Answer.Point queryPoint = new Answer.Point(2, 2);
        int k = 3;

        Answer.Point[] result = knn.findKNearestNeighbors(points, queryPoint, k);

        assertEquals(0, result.length);
    }

    @Test
    public void testFindKNearestNeighbors_AllPointsEquidistant() {
        Answer knn = new Answer();
        Answer.Point[] points = {
                new Answer.Point(2, 3),
                new Answer.Point(3, 2),
                new Answer.Point(1, 2),
                new Answer.Point(2, 1)
        };
        Answer.Point queryPoint = new Answer.Point(2, 2);
        int k = 2;

        Answer.Point[] result = knn.findKNearestNeighbors(points, queryPoint, k);

        assertEquals(2, result.length);
        assertTrue(containsPoint(result, new Answer.Point(2, 3)));
        assertTrue(containsPoint(result, new Answer.Point(3, 2)));
    }

    private boolean containsPoint(Answer.Point[] points, Answer.Point point) {
        for (Answer.Point p : points) {
            if (Math.abs(p.x - point.x) < 0.001 && Math.abs(p.y - point.y) < 0.001) {
                return true;
            }
        }
        return false;
    }
}
