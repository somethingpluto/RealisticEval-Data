package org.real.temp;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.List;

import org.real.temp.Answer;

public class Tester {

    private List<Point> square;
    private List<Point> triangle;
    private List<Point> concave;

    @Before // Updated annotation for JUnit 5
    public void setUp() {
        // Define some polygons to use in tests
        square = new ArrayList<>();
        square.add(new Point(0, 0));
        square.add(new Point(0, 10));
        square.add(new Point(10, 10));
        square.add(new Point(10, 0));

        triangle = new ArrayList<>();
        triangle.add(new Point(0, 0));
        triangle.add(new Point(5, 10));
        triangle.add(new Point(10, 0));

        concave = new ArrayList<>();
        concave.add(new Point(0, 0));
        concave.add(new Point(5, 5));
        concave.add(new Point(10, 0));
        concave.add(new Point(5, 10));
        concave.add(new Point(0, 10));
    }

    @Test
    public void testPointInsideSquare() {
        // Point inside the square
        assertTrue(Answer.isPointInPolygon(new Point(5, 5), square));
    }

    @Test
    public void testPointOutsideSquare() {
        // Point outside the square
        assertFalse(Answer.isPointInPolygon(new Point(15, 5), square));
    }

    @Test
    public void testPointOnEdgeOfTriangle() {
        // Point on the edge of the triangle
        assertFalse(Answer.isPointInPolygon(new Point(5, 0), triangle));
    }

    @Test
    public void testPointInsideConcavePolygon() {
        // Point inside concave polygon
        assertTrue(Answer.isPointInPolygon(new Point(5, 9), concave));
    }

    @Test
    public void testPointOutsideConcavePolygon() {
        // Point outside concave polygon
        assertFalse(Answer.isPointInPolygon(new Point(5, 1), concave));
    }


}
