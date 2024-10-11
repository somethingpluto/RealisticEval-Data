package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Use Bresenham line algorithm to generate a straight line between two points,
     * returning all the points that the line passes through.
     *
     * @param x1 Coordinates of the start point x.
     * @param y1 Coordinates of the start point y.
     * @param x2 Coordinates of the end point x.
     * @param y2 Coordinates of the end point y.
     * @return List of points (tuples of x and y coordinates) that the line passes through.
     */
    public static List<Point> bresenhamLine(int x1, int y1, int x2, int y2) {
        List<Point> points = new ArrayList<>();

        // ... rest of your Bresenham implementation goes here ...

        return points;
    }

    // Define a Point class since there isn't one in Java
    public static class Point {
        private int x;
        private int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }
    }
}